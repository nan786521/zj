while True:
    try:
        n=int(input())
        ans=1
        for i in range(n-1):
            ans+=i+1
        print(ans)
    except:
        break
