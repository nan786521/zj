ans=0
for i in range(2):
    a1,a2,a3,a4=map(int,input().split())
    b1,b2,b3,b4=map(int,input().split())
    sa=a1+a2+a3+a4
    sb=b1+b2+b3+b4
    print("%d:%d" % (sa,sb))
    if sa>sb:
        ans+=1
    elif sa<sb:
        ans-=1
if ans==0:
    print("Tie")
elif ans>=1:
    print("Win")
else:
    print("Lose")
