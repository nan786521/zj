a1,b1,c1=map(int,input().split())
a2,b2,c2=map(int,input().split())
n=int(input())
max=-999999
for i in range(n+1):
    y1=a1*(i**2)+b1*i+c1
    y2=a2*((n-i)**2)+b2*(n-i)+c2
    if y1+y2>max:
        max=y1+y2
print(max)
