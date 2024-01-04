n=int(input())
for i in range(n):
    f=1
    ans=""
    d1=list(map(int,input().split()))
    d2=list(map(int,input().split()))
    if d1[1]==d1[3] or d2[1]==d2[3] or d1[1]!=d1[5] or d2[1]!=d2[5]:
        ans=ans+"A"
        f=0
    if d1[6]!=1 or d2[6]!=0:
        ans=ans+"B"
        f=0
    if d1[1]==d2[1] or d1[3]==d2[3] or d1[5]==d2[5]:
        ans=ans+"C"
        f=0
    if f:
        print("None")
    else:
        print(ans)
