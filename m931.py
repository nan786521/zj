n=int(input())
d=[]
for i in range(n):
    a,b=map(int,input().split())
    d.append(a)
    d.append(b)
    d.append(a**2+b**2)
#print(d)
t=d.index(max(d))-2
#print(d.index(max(d)))
#d.pop(d.index(max(d)))
d.pop(t)
d.pop(t)
d.pop(t)
t=d.index(max(d))
print(d[t-2],d[t-1])
