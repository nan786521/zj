n=int(input())
d=list(map(int,input().split()))
ans=0
for i in range(n):
    ans+=(i+1)*d[i]
print(ans)
