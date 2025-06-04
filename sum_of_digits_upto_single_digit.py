n=9789
def digit_sum(n):
    total = 0
    while n:
        total+=n%10
        n//=10
    if total>=10:
        digit_sum(total)
    else:
        print("The single digit after all sum is",total)
digit_sum(n)

#  OR

n=9789
while n>9:
    total = 0
    while n:
        total += n % 10
        n //= 10
    n=total
print(n)