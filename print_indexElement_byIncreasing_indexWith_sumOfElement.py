n=[1,2,3,4,5]
if 0 in n:
    print(-1)
else:
    i=0
    while i < len(n):
        print(n[i],end=" ")
        i+=n[i]