a,b=[int(a) for a in input().split()]
print(a,b)
list1=[]
sum=0
for i in range(a):
      c=int(input())
      list1.insert(i,c)
print(list1)
for j in range(b):
      sum=sum+list1[j]
print(sum)
