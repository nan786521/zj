n=int(input())
while n!=0:
    for i in range(1,n):
        if i%7!=0:
            print(i,end=" ")
    print()
    n=int(input())
