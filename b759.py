n=input()
d=[]
print(n)
for i in range(len(n)):
    d.append(n[i])
for i in range(len(n)-1):
    d.append(d.pop(0))
    for j in d:
        print(j,end="")
    print()
