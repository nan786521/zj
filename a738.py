while True:
    try:
        a,b=map(int,input().split())
        while b!=0:
            t=a%b
            a=b
            b=t
        print(a)
    except:
        break
