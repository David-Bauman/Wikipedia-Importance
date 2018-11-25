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

counter = 0

def get_text(page, url_list, importance):
    global counter
    while True:
        try:
            soup = BeautifulSoup(urlopen("https://wikipedia.org/wiki/"+\
            page).read(), "lxml").find_all('a')

            #finds all the url links to other wikipedia pages within the html
            for a in soup:
                href = str(a.get('href'))
                if href[0:6] == "/wiki/":
                    href = href[6:]
                    if not ('#' in href or ':' in href or "Main_Page" == href):
                        if href in importance:
                            importance[href] += 1
                        else:
                            importance[href] = 1
                            url_list.append(href)
            counter += 1
            page = url_list.pop()
        except (FileNotFoundError, NotADirectoryError, HTTPError):
            continue
        except IndexError:
            return


def main():
    global counter
    start_time = time.time()

    url_list = []
    importance = {}
    #if there's already files e.g. the program has been restarted after a
    #"pause", reads the files and adds all the info to the structures
    try:
        with open("url_list") as f:
            url_list = f.read().splitlines()
        page = url_list.pop()
        with open("importance") as f:
            for line in f:
                line = line.strip()
                key, val = line.split('#')
                importance[key] = int(val)
    except (FileNotFoundError, IndexError):
        page = "Mango"
        importance[page] = 0

    print("Getting from files takes %.2f seconds\n" % (time.time() - start_time))
    start_time = time.time()
    try:
        get_text(page, url_list, importance)
        print("\n\nThat's a wrap folks. ")
        print("Total files: ", len(importance))
        raise KeyboardInterrupt

    #since all other exceptions are taken care of, all that's left is if the
    #user "pauses". if they do, throw the current info to some files.
    except (KeyboardInterrupt, SystemExit, URLError):
        total_time = time.time() - start_time
        s = "\n\n%s urls were searched in %s seconds, good for %s " \
         "pages/second. %s urls to go.\n" % (format(counter, ',d'),\
         format(total_time, ',.2f'), format(counter/total_time, ',.2f'),\
         format(len(url_list), ',d'))
        print(s)

        start_time = time.time()
        save(url_list, importance)
        print("\nWriting to files took %.2f seconds" % (time.time()-start_time))

def save(url_list, importance):
    with open("url_list", "w") as f:
        for item in url_list:
            f.write(item + "\n")
    with open("importance", "w") as f:
        for k, v in importance.items():
            f.write("%s#%d\n" % (k, v))
    return

main()
