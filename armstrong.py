n=int(input())
temp=n
count=0
while n:
    n//=10
    count+=1
print(count)
sum=0
n=temp
while n:
    x=n%10
    sum+=x**count
    n//=10
if(temp==sum):
    print(temp," is armstrong")
else:
    print(temp," is not armstrong")