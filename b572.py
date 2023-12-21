n=int(input())
for i in range(n):
    d=list(map(int,input().split()))
    t1=d[0]*60+d[1]
    t2=d[2]*60+d[3]
    if t1+d[4]<=t2:
        print("Yes")
    else:
        print("No")
