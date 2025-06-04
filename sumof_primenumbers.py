n=98762
sum=0
while n:
    x=n%10
    for i in range(2,(x//2)+1):
        if x%i==0:
            break
    else:
        sum+=x
    n//=10
print(sum)

#  OR

n=98762
sum=0
while n:
    x=n%10
    if x in [2,3,5,7]:
        sum+=x
    n//=10
print(sum)