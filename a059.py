n=int(input())
for i in range(n):
    a=int(input())
    b=int(input())
    ans=0
    for j in range(a,b+1):
        if (j**0.5)**2==(int(j**0.5))**2:
            ans+=j
    print("Case %d: %d" % (i+1,ans))
