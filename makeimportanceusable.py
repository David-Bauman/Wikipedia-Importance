def main():
    infile = open("importance_list","r")
    data = []
    word = True
    next_place = 0
    for line in infile:
        line = line.strip()
        if word:
            data.append([line])
            word = False
        else:
            data[next_place].append(int(line))
            word = True
            next_place += 1
    top_twenty = []
    total_refs = 0
    total_referenced_pages = len(data)
    quickfile = open("searched_pages_list","r")
    total_searched_pages = 0
    for line in quickfile:
        total_searched_pages += 1
    quickfile.close()
    for item in data:
        total_refs += item[1]
    for x in range(20):
        best = ["",0]
        for item in data:
            if item[1] > best[1]:
                best = item
        top_twenty.append(best)
        data.remove(best)
    for item in top_twenty:
        print("%s: %d"%(item[0].replace('_'," "),item[1]))

    print("\n\n# of total references: %d"%(total_refs))
    print("# of pages referenced: %d"%(total_referenced_pages))
    print("Average # of references to each page: %.2f"%(total_refs/total_referenced_pages))
    print("Average # of references per page scanned: %.2f"%(total_refs/total_searched_pages))

main()
