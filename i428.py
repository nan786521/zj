n=int(input())
max=-99999
min=99999
x1,y1=map(int,input().split())
for i in range(n-1):
    x2,y2=map(int,input().split())
    if abs(x1-x2)+abs(y1-y2)>max:
        max=abs(x1-x2)+abs(y1-y2)
    if abs(x1-x2)+abs(y1-y2)<min:
        min=abs(x1-x2)+abs(y1-y2)
    x1=x2
    y1=y2
print(max,min)
