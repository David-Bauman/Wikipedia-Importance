from queue import PriorityQueue

def main():
    infile = open("importance","r")
    data = PriorityQueue()
    totalref = 0
    for line in infile:
        line = line.strip()
        key, val = line.split('#')
        totalref += int(val)
        data.put((0-int(val),key))
    infile.close()

    totalpages = data.qsize()
    acc = sum(1 for line in open("searched_pages","r"))

    for i in range(20):
        best = data.get()
        print("%s: %d"%(best[1].replace("_"," "),abs(best[0])))

    print("\n\n# of total references to other pages: %s"\
    %(format(totalref,',d')))

    print("# of pages referenced: %s"%(format(totalpages,',d')))
    print("Average # of references to each page: %s"\
    %(format(totalref/totalpages,',.2f')))
    
    print("# of references per page scanned: %s"%(format(totalref/acc,',.2f')))

main()
