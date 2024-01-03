n=int(input())
d=list(map(int,input().split()))
d.insert(0,999)
d.append(999)
ans=0
for i in range(1,n+1):
    if d[i]==0:
        if d[i-1]>d[i+1]:
            ans+=d[i+1]
        else:
            ans+=d[i-1]
print(ans)
