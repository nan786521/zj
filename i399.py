d=list(map(int,input().split()))
d.sort()
if d[0]==d[1] and d[1]==d[2]:
    print("3",d[0])
elif d[0]==d[1] or d[1]==d[2]:
    print("2",d[2],d[0])
else:
    print("1",d[2],d[1],d[0])
