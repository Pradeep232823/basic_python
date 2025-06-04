def small(n,i=0):
    if i==len(n)-1:
        return n[i]
    return min(n[i],small(n,i+1))
print(small([342,532,123,323,324]))