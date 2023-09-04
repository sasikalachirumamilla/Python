d=0
n=int(input())
for i in range(1,n+1):
    if n%i==0:
        d=d+1
if d==2:
    print("Prime Number")
else:
    print("Not a prime Number")