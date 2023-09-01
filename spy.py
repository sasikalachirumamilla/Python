#Spy Number
n=int(input())
s=0;m=1
while n>0:
    r=n%10
    s+=r
    m*=r
    n=n//10
if s==m:
    print("Spy Number")
else:
    print("Not a Spy Number")