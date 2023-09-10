#Amicable Numbers
#Amicable numbers are two natural numbers related in such a way that the sum of the proper divisors of each is equal to the other number.
n=int(input())
m=int(input())
s1=0;s2=0
for i in range(1,n):
    if n%i==0:
        s1+=i
for i in range(1,m):
    if m%i==0:
        s2+=i
if s1==m and s2==n:
    print("Amicable Numbers")
else:
    print("Not Amicable Numbers")