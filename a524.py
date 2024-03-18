import itertools
while True:
    try:
        n=int(input())
        t=""
        for i in range(n):
            t=t+str(i+1)
        ans=[]
        r = itertools.permutations(t)
        for i in r:
            ans.append(i)
            #print(*i)
        ans.sort(reverse=True)
        for i in range(len(ans)):
            for j in range(len(ans[0])):
                print(ans[i][j],end="")
            print()
    except:
        break
