def main():
    infile = open("importanceofpages","r")
    data = []
    word = True
    nextplace = 0
    for line in infile:
        line = line.strip()
        if word:
            data.append([line])
            word = False
        else:
            data[nextplace].append(int(line))
            word = True
            nextplace += 1
    bestlstEU = []
    totalref = 0
    totalpages = len(data)
    quickfile = open("havethefileslst","r")
    acc = 0
    for line in quickfile:
        acc += 1
    for item in data:
        totalref += item[1]
    for x in range(20):
        best = ["",0]
        for item in data:
            if item[1] > best[1]:
                best = item
        bestlstEU.append(best)
        data.remove(best)
    for bestest in bestlstEU:
        word = bestest[0]
        cleanedword = ""
        for ch in word:
            if ch == "_":
                cleanedword += " "
            else:
                cleanedword += ch
        print("%s: %d"%(cleanedword,bestest[1]))

    print("\n\n# of total references: %d"%(totalref))
    print("# of pages referenced: %d"%(totalpages))
    print("Average # of references to each page: %.2f"%(totalref/totalpages))
    print("Average # of references per page scanned: %.2f"%(totalref/acc))

main()
