n=6
if n<=1:
    print(n)
else:
    first=0
    second=1
    for i in range(2,n+1):
        third=first+second
        first=second
        second=third
    print(third)