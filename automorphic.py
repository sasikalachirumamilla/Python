#Automorphic Number
n=int(input())
sq=n**2
flag=0
while n>0:
    if n%10==sq%10:
        n//=10
        sq//=10
    else:
        flag=1
        break
if flag==0:
    print("Automorphic Number")
else:
    print("Not a Automorphic Number")