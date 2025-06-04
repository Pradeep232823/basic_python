password=123

while True:
    print("enter the password ")
    n=int(input())
    if n==password:
        print("login successful")
        break
    else:
        print("login fail")