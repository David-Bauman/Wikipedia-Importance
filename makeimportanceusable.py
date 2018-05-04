from queue import PriorityQueue

def main():
    data = PriorityQueue()
    totalref = 0
    infile = open("importance","r")
    for line in infile:
        line = line.strip()
        key, val = line.split('#')
        totalref += int(val)
        data.put((0-int(val),key))
    infile.close()

    totalpages = data.qsize()

    for i in range(20):
        best = data.get()
        print("%s: %s"%(best[1].replace("_"," "),format(abs(best[0]),',d')))

    print("\n\n# of total references to other pages: %s"\
    %(format(totalref,',d')))

    print("# of pages referenced: %s"%(format(totalpages,',d')))
    print("Average # of references to each page: %s"\
    %(format(totalref/totalpages,',.2f')))


main()
