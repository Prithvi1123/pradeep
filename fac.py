a=int(input())
f=1
if(a>0):
    for i in range(1,a+1):
        f=f*i
    print(f)
elif(a==0):
    f=1
    print(f)
else:
    print("invalid")
