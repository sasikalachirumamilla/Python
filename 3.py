n=input("Enter String:")
l=[]
for i in range(len(n)):
    l.append(n[i])
for i in range(len(l)):
    c=chr(ord(l[i])+3)
    c=str(c)
    l[i]=[c]
print(*(l))
n=input("Enter:")
d=chr(ord(n)+3)
print(d)