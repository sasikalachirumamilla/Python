n=int(input("Enter:"))
l=[]
for i in range(n):
    e=int(input("enter:"))
    l.append(e)
r=max(l)
l.pop(l.index(r))
print(l)
a=max(l)
a=int(a)
r=int(r)
print("biggest numbers are:",r,a)
print("sum:",r+a)
print("Multiply:",r*a)