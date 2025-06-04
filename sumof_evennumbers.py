n=98762
sum=0
while n:
    x=n%10
    if x%2==0:
        sum+=x
    n//=10
print(sum)