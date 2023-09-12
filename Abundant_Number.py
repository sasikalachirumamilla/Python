#Abundant_Number
#Abundant number is a positive integer for which the sum of its proper divisors is greater than the given number.
n=int(input())
s=0
for i in range(1,n):
    if n%i==0:
        s+=i
if s>n:
    print("Abundant Number")
else:
    print("Not a Abundant Number")