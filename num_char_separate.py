n="Hi087b59saer31"
characters=""
numbers=""
for i in n:
    if 65<= ord(i) <=90 or 97<= ord(i) <=122:
        characters+=i
    elif 48<=ord(i)<=57:
        numbers+=i
print(numbers, end=" ")
print(characters, end=" ")

n="Hi087b59saer31"
char=""
num=""
for i in n:
    if 65<= ord(i) <=90 or 97<= ord(i) <=122:
        char+=i
    else:
        num+=i
print(char, num)