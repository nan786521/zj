n,d=map(int,input().split())
a=list(map(int,input().split()))
f=1
x=a[0]
ans=0
for i in range(1,n):
    if a[i]>=x+d and f==1:
        f=0
        ans=ans+a[i]-x
        x=a[i]
    if a[i]<=x-d and f==0:
        f=1
        x=a[i]
print(ans)
