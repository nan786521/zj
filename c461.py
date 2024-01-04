a,b,c=map(int,input().split())
if a!=0:
    a=1
if b!=0:
    b=1
if a==0 and b==0 and c==1:
    print("IMPOSSIBLE")
else:
    if (a and b) == c:
        print("AND")
    if (a or b) == c:
        print("OR")
    if (a ^ b) == c:
        print("XOR")
