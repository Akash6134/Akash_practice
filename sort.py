def my_sorting(lisst):
    for i in range(0,len(lisst)):
        for j in range(i+1,len(lisst)):
            if lisst[i]>lisst[j]:
                temp = lisst[i]
                lisst[i] = lisst[j]
                lisst[j] = temp
    return lisst