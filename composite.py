n=int(input()) # input
if(n>1):
    for i in range(2,n):#for loop
        if(n%i==0):
            print("yes")
            break
    else:
        print("no")
else:
    print("yes")
