def evenSum():
    n=[4,5,35,71,1,2]
    for i in range(len(n)):
        sum=i+n[i]
        if sum%2==0:
            print("sum of index ",i," and element ",n[i]," is even that is: ",sum)
        else:
            print("sum of index ",i," and element ",n[i]," is odd that is: ",sum)
evenSum()