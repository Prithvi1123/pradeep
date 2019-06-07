a,b=[int(a) for a in input().split()]
c=a+1
co=0
for i in range(c,b):
    for j in range(1,i+1):
        if(i%j==0):
            co=co+1
    if(co==2):
        print(i,end=' ')
    co=0
