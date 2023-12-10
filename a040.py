a,b=map(int,input().split())
f=1
for i in range(a,b+1):
    t=len(str(i))
    d=str(i)
    s=0
    for j in range(t):
        s+=int(d[j])**t
    if i==s:
        f=0
        print(i,end=" ")
if f:
    print("none")
else:
    print()
