while True:
    try:
        n=int(input())
        s=0
        for i in range(1,(n//2)+1):
            if n%i==0:
                s+=i
        if s>n:
            print("盈數")
        elif s<n:
            print("虧數")
        else:
            print("完全數")
    except:
        break
