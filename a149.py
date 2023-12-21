n=int(input())
for i in range(n):
    d=input()
    ans=int(d[0])
    for j in range(1,len(d)):
        ans*=int(d[j])
    print(ans)
