"""
This creates a textfile of importance of wikipedia pages (to be used in
conjunction with makeimportanceusable.py). The program can be "paused" by
quitting (Ctrl+C) and came back to later simply by running it again. It will
pick back up where it left off.
David Bauman, 2017 - 12 - 19
"""
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import time

def get_text(page, url_list, importance, searched_pages):
    try:
        if page in searched_pages:
            raise Exception("We've already done this one: ",page)
        soup = BeautifulSoup(urlopen("https://wikipedia.org/wiki/"+\
        page).read(), "lxml")
        searched_pages[page] = 0

        #finds all the url links to other wikipedia pages within the html
        for a in soup.find_all("a"):
            href = str(a.get('href'))
            if href[0:6] == "/wiki/":
                href = href[6:]
                if not ('#' in href or ':' in href or "Main_Page" == href):
                    writing(href,importance)
                    if not (href in searched_pages):
                        putithere,alreadyhere = binary_search(url_list, href)
                        if not alreadyhere:
                            url_list.insert(putithere, href)
    except (FileNotFoundError, NotADirectoryError, HTTPError):
        pass

    if len(url_list) == 0:
        return False
    return url_list.pop()

def binary_search(lst, search):
    low = 0
    high = len(lst)-1
    while high >= low:
        mid = int((high+low)/2)
        if lst[mid] == search:
            return mid,True
        elif lst[mid] < search:
            low = mid + 1
        else:
            high = mid - 1
    return low,False

def writing(key, dictionary):
    if key in dictionary:
        dictionary[key] += 1
    else:
        dictionary[key] = 1
    return

def main():
    page = "Mango"
    start_time = time.time()

    #if there's already a url_list e.g. the program has been restarted after a
    #"pause", reads the file and appends to the list all the info
    url_list = []
    try:
        infile = open("url_list","r")
        url_list = infile.read().splitlines()
        page = url_list.pop()
        infile.close()
    except (FileNotFoundError,IndexError):
        pass

    #same as above but for a searched_pages dict
    searched_pages = {}
    try:
        infile = open("searched_pages","r")
        for line in infile:
            line = line.strip()
            searched_pages[line] = 0
        infile.close()
    except FileNotFoundError:
        pass

    #same as above
    importance = {}
    try:
        infile = open("importance","r")
        for line in infile:
            line = line.strip()
            key,val = line.split('#')
            importance[key] = int(val)
    except FileNotFoundError:
        pass

    print("Getting from files takes %.2f seconds\n" %(time.time()-start_time))
    start_len = len(searched_pages)
    start_time = time.time()
    try:
        while True:
            page = get_text(page, url_list, importance, searched_pages)
            #if by God's good grace it's over
            if page == False:
                print("\n\nthat's a wrap folks")
                print("total files: ",len(searched_pages))
                raise KeyboardInterrupt

    #since all other exceptions are taken care of, all that's left is if the
    #user "pauses". if they do, throw the current info to some files.
    except (KeyboardInterrupt, SystemExit, URLError):
        total_time = time.time()-start_time
        total_files = len(searched_pages)- start_len
        s = "\n\n%s urls were searched in %s seconds, good for %s " \
         "pages/second and a total of %s pages.\n"%(format(total_files,',d'),\
        format(total_time,',.2f'),format(total_files/total_time,',.2f'),\
        format(len(searched_pages),',d'))
        print(s)

        start_time = time.time()
        save(url_list, searched_pages, importance)
        print("\nWriting to files took %.2f seconds" % (time.time()-start_time))

def save(url_list, searched_pages, importance):
    newfile = open("url_list","w")
    for item in url_list:
        newfile.write(item + "\n")
    newfile.close()
    newfile = open("searched_pages","w")
    for item in list(searched_pages.keys()):
        newfile.write(item + "\n")
    newfile.close()
    infile = open("importance","w")
    for k, v in importance.items():
        infile.write("%s#%d\n" % (k, v))
    infile.close()

main()
