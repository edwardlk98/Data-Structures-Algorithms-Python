def groupingTransaction(n:list):
    dct = dict()
    ls = []
    try: 
        for i in n:
            dct[i] = dct.get(i,0) + 1
        lst = list(dct)  
        for i in range(len(dct)):
            for j in range(i+1,len(dct)):
                if (dct[lst[j]] > dct[lst[i]]):
                    t = lst[i]
                    lst[i] = lst[j]
                    lst[j] = t                                     
                if (dct[lst[i]] == dct[lst[j]]):
                      if lst[j]  < lst[i]:
                          t = lst[i]
                          lst[i] = lst[j]
                          lst[j] = t
        for i in range(len(lst)):
            s = str(dct[lst[i]])
            stri = lst[i] + " " + s
            ls.append(stri)
            pass
        return ls

    except:
        print("Must provide a list of transaction")
    

print(groupingTransaction(['notebook', 'notebook', 'mouse', 'keyboard', 'mouse']))
