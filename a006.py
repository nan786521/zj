a,b,c=map(int,input().split())
t=b**2-4*a*c
if t>0:
    print("Two different roots x1=%d , x2=%d" % ((-b+t**0.5)/(2*a),(-b-t**0.5)/(2*a)))
elif t==0:
    print("Two same roots x=%d" % ((-b+t**0.5)/(2*a)))
else:
    print("No real root")
