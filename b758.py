h,m=map(int,input().split())
t=h*60+m+150
if t>=1440:
    t-=1440
h=t//60
m=t%60
if h<10:
    print("0%d:" % (h),end="")
else:
    print("%d:" % (h),end="")
if m<10:
    print("0%d" % (m))
else:
    print("%d" % (m))
