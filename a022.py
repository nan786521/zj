n=input()
f=1
for i in range(len(n)//2):
    if n[i]!=n[len(n)-i-1]:
        f=0
if f:
    print("yes")
else:
    print("no")
