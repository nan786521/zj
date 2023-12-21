ans=input()
n=int(input())
for i in range(n):
    g=input()
    a,b=0,0
    for j in range(4):
        for k in range(4):
            if ans[j]==g[k]:
                if j==k:
                    a+=1
                else:
                    b+=1
    print("%dA%dB" % (a,b))
