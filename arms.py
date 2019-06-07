a,b=[int(a) for a in input().split()]
for l1 in range(a,b):
  sum=0
  c=l1
  while(l1!=0):
    rem=l1%10
    sum=sum+rem*rem*rem
    l1=l1//10
  if (c==sum):
    print(c,end=" ")
