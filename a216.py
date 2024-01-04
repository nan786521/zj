while True:
    try:
        n=int(input())
        f=n*(n+1)/2
        g=f*(n+1)-n*(n+1)*(2*n+1)/6
        print(int(f),int(g))
    except:
        break

'''
def f(n):
    if n==1:
        return 1
    else:
        return n+f(n-1)

def g(n):
    if n==1:
        return 1
    else:
        return f(n)+g(n-1)

while True:
    try:
        n=int(input())
        print(f(n),g(n))
    except:
        break
'''
