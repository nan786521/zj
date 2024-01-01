n,d=map(int,input().split())
ans=0
c=0
for i in range(n):
    data=list(map(int,input().split()))
    data.sort()
    if abs(data[0]-data[2])>=d:
        ans=ans+sum(data)//3
        c+=1
print(c,ans)
