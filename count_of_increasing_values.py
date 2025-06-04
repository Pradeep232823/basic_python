n = 134532
x = str(n)
count = 1
for i in range(len(x) - 1):

    if x[i] < x[i + 1]:
        count += 1
    else:
        break
print("The increasing values count is", count)
