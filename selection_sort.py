def Selection_sort(a):
    for phase in range(len(a)-1):
        min = phase
        for i in range(phase+1, len(a)):
            if a[i]<a[min]:
                min = i
        if min != phase: a[min],a[phase] = a[phase] , a[min]
    return a
a = [ 21 ,18,61,45,81,10]
print( Selection_sort(a) )