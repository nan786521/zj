x,n=map(int,input().split())
right=0
left=0
max_p=-100
min_p=100
d=list(map(int,input().split()))
for i in range(n):
    t=d[i]
    if t>x:
        right+=1
    else:
        left+=1
    if t>max_p:
        max_p=t
    if t<min_p:
        min_p=t
if right>left:
    print(right,max_p)
else:
    print(left,min_p)
