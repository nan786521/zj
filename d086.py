d=input()
while d!="0":
    s=0
    f=1
    for i in d:
        if ord(i.lower())-96>=0 and ord(i.lower())-96<=26:
            s=s+ord(i.lower())-96
        else:
            f=0
            break
    if f:
        print(s)
    else:
        print("Fail")
    d=input()
