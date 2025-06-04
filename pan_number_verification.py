def panverify(pan):
    if len(pan)!=10:
        print("not valid pan number")
    upper=digit=None
    for i in range(0,5):
        if pan[i].isalpha():
            upper=pan[i].isupper()
    for i in range(5,9):
        digit = pan[i].isdigit()
    for i in range(9,10):
        upper=pan[i].isupper()
    if upper and digit:
        return True
    return False

pan=input()
print( panverify(pan) )