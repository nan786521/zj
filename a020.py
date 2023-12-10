location=[10,11,12,13,14,15,16,17,34,18,19,20,21,22,35,23,24,25,26,27,28,29,32,30,31,33]
n=input()
t=location[ord(n[0])-65]
t=t%10*9+t//10
for i in range(1,9):
    t+=int(n[i])*(9-i)
    #print(int(n[i+1])*(9-i))
    #print(int(n[i]))
t+=int(n[9])
if t%10==0:
    print("real")
else:
    print("fake")
