def a(n):
    if n==1:
        return
    a(n-1)
    print(n, end=" ")
    a(n-1)
a(5)