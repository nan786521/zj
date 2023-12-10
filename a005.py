n=int(input())
for i in range(n):
    a1,a2,a3,a4=map(int,input().split())
    if a4-a3==a2-a1:
        print(a1,a2,a3,a4,a4+(a4-a3))
    else:
        print(a1,a2,a3,a4,int(a4*(a4/a3)))
