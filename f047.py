d=list(map(str,input().split()))
one=[]
two=[]
three=[]
for i in range(len(d)):
    if i%3==0:
        one.append(d[i])
    elif i%3==1:
        two.append(d[i])
    else:
        three.append(d[i])
for i in one:
    print(i,end=" ")
print()
for i in two:
    print(i,end=" ")
print()
for i in three:
    print(i,end=" ")
print()
