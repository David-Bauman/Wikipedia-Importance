"""
This creates a textfile of importance of wikipedia pages (to be used in conjunction
with makeimportanceusable.py). The program can be "paused" by quitting (Ctrl+C) and came
back to later simply by running it again. It will pick back up where it left off.
David Bauman, 2017 - 12 - 19
"""
from bs4 import BeautifulSoup
from urllib.request import *
from urllib.error import *
import time

def get_text(firstparturl,url_list,importance_list,searched_pages_list):
    try:
        url = "https://wikipedia.org/wiki/"+firstparturl
        html = urlopen(url).read()
        soup = BeautifulSoup(html)
        putitheretwo,eh = binary_search(searched_pages_list,firstparturl)
        if not eh:
            searched_pages_list.insert(putitheretwo,firstparturl)
        else:
            raise Exception("Houston we've had a problem: ",firstparturl)

        #finds all the url links to other wikipedia pages within the html
        for a in soup.find_all("a"):
            href = str(a.get('href'))
            if href[0:6] == "/wiki/":
                href = href[6:]
                if not ('#' in href or ':' in href or "Main_Page" == href):
                    writing(href,importance_list)
                    putithere,alreadyhere = binary_search(url_list,href)
                    if not alreadyhere:
                        ignore,inhere = binary_search(searched_pages_list,href)
                        if not inhere:
                            url_list.insert(putithere,href)

    except (FileNotFoundError,NotADirectoryError,HTTPError):
        pass

    if len(url_list) == 0:
        return False
    else:
        return url_list.pop(0)

def binary_search(lst,search):
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


#binary search to find if the W.page has already been referenced before. if so,
#increments its count by 1. otherwise appends a list at the proper place
def writing(search,lst):
    Valid = False
    low = 0
    high = len(lst) - 1
    while low <= high:
        middle = int((low + high)/2)
        if search == lst[middle][0]:
            Valid = True
            break
        elif search > lst[middle][0]:
            low = middle + 1
        else:
            high = middle -1
    if Valid:
        lst[middle][1] += 1
    else:
        lst.insert(low,[search,1])
    return

def main():
    firstparturl = "Mango"
    starttime = time.time()

    #if there's already a url_list i.e. the program has been restarted after a "pause"
    #reads the file and appends to the list all the info
    url_list = []
    try:
        infile = open("url_list","r")
        url_list = infile.read().splitlines()
        firstparturl = url_list.pop(0)
        infile.close()
    except (FileNotFoundError,IndexError):
        pass

    #same as above but for searched_pages_list
    searched_pages_list = []
    try:
        infile = open("searched_pages_list","r")
        searched_pages_list = infile.read().splitlines()
        infile.close()
    except FileNotFoundError:
        pass

    #same as above
    importance_list = []
    try:
        infile = open("importance_list","r")
        word = True
        nextplace = 0
        for line in infile:
            line = line.strip()
            if word:
                importance_list.append([line])
                word = False
            else:
                importance_list[nextplace].append(int(line))
                word = True
                nextplace += 1
    except FileNotFoundError:
        pass

    print("Getting from files takes %f seconds\n" %(time.time()-starttime))
    startlength = len(searched_pages_list)
    starttime = time.time()
    try:
        while True:
            firstparturl = get_text(firstparturl,url_list,importance_list,searched_pages_list)
            #if by God's good grace it's over
            if firstparturl == False:
                print("\n\nthat's a wrap folks")
                print("total files: ",len(searched_pages_list))
                raise KeyboardInterrupt

    #since all other exceptions are taken care of, all that's left is if the user "pauses"
    #if they do, throw the current info to some files.
    except (KeyboardInterrupt,SystemExit,URLError):
        totaltime = time.time()-starttime
        totalfiles = len(searched_pages_list)- startlength
        print("\n\nIn %.1f seconds %d urls were searched through, good for %f pages/second and a total of %d pages.\n"%(totaltime,totalfiles,totalfiles/totaltime,len(searched_pages_list)))
        writingtime = time.time()
        save(url_list,searched_pages_list,importance_list)
        print("\nWriting to files took %f seconds" % (time.time()-writingtime))

def save(url_list, searched_pages_list, importance_list):
    newfile = open("url_list","w")
    for item in url_list:
        newfile.write(item + "\n")
    newfile.close()
    newfile = open("searched_pages_list","w")
    for item in searched_pages_list:
        newfile.write(item + "\n")
    newfile.close()
    infile = open("importance_list","w")
    for item in importance_list:
        for i in [0,1]:
          infile.write(str(item[i]))
          infile.write("\n")
    infile.close()

main()
