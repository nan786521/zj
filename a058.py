n=int(input())
a,b,c=0,0,0
for i in range(n):
    d=int(input())
    if d%3==0:
        a+=1
    elif d%3==1:
        b+=1
    else:
        c+=1
print("%d %d %d" % (a,b,c))
