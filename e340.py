n=int(input())
d=list(map(int,input().split()))
print(d[0],end=" ")
for i in range(n-1):
    print(d[i+1]-d[i],end=" ")
