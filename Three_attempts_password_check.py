password=123

for i in range(3):
    print("enter the password ")
    n=int(input())
    if n==password:
        print("login successful")
        break
    else:
        print(i+1,"attempts is done in 3 attempts",3-i-1,"attempts remain")
else:
    print("login fail and account blocked")