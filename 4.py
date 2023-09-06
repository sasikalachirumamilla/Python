n=input("Enter string:")
l=[]
for i in range(len(n)):
    l.append(n[i])
for i in range(len(l)):
    s=0
    c=l.count(l[i])
    if(s<c):
        s=l[i]
print(s)