d=list(map(str,input().split()))
for i in range(len(d)-2):
    print(d[i+1],d[0],end=" ")
print(d[-1])
