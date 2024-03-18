while True:
    try:
        x,y=map(int,input().split())
        test = [[0] * y for _ in range(x)]
        for i in range(x):
            test[i]=list(map(int,input().split()))
        #print(list((zip(*test))))
        ans=list((zip(*test)))
        for i in range(y):
            for j in ans[i]:
                print(j,end=" ")
            print()
    except:
        break
