s=int(input())
a=1 
b=1 
c=0
print(a,b,end=" ")
for i in range(2,s):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
