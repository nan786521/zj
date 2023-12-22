while True:
    try:
        d=list(map(int,input().split()))
        if (sum(d)-d[0])/d[0]>59:
            print("no")
        else:
            print("yes")
    except:
        break
