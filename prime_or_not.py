
n=2
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
print("prime" if count==2 else "not prime")

# OR

# n=2
# count=0
# if n==2:
#     print("prime")
# for i in range(2,n):
#     if n%i==0:
#         print("not prime")
#     else:
#         ("prime")