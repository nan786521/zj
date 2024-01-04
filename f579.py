a,b=map(int,input().split())
ans=0
n=int(input())
for i in range(n):
    c_a=0
    c_b=0
    d=list(map(int,input().split()))
    for j in range(len(d)):
        if d[j]<0:
            if abs(d[j])==a:
                c_a-=1
            elif abs(d[j])==b:
                c_b-=1
        else:
            if d[j]==a:
                c_a+=1
            elif d[j]==b:
                c_b+=1
    if c_a!=0 and c_b!=0:
        ans+=1
print(ans)
