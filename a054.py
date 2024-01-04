d=[10,11,12,13,14,15,16,17,34,18,19,20,21,22,35,23,24,25,26,27,28,29,32,30,31,33]
ans=""
for i in range(len(d)):
    d[i]=d[i]//10+(d[i]%10)*9
n=input()
s=0
for i in range(8):
    #print(int(n[i])*(8-i))
    s+=int(n[i])*(8-i)
s+=int(n[8])
#print(chr(ord("A")+1))
for i in range(len(d)):
    if (s+d[i])%10==0:
        ans=ans+chr(ord("A")+i)
print(ans)
