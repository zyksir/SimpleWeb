def sort_age(lst):
    result = []
    while lst !=[]:
        k = lst[0][1]
        index = 0
        for i in range(1,len(lst)):
            if lst[i][1] < k:
                index = i
                k = lst[i][1]
        result = result +[lst[index]]
        lst.pop[index]
    return result