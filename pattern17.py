# a
# b b
# c c c

n=26
for i in range(0,n):
    for j in range(0,i+1):
        print( chr(ord("a") +i),end=" ")
    print()