n1 = int(input())  
s1 = 0  
t1 = n1  
while t1 > 0:  
   d1 = t1 % 10  
   s1 += d1 ** 3  
   t1 //= 10  
if n1 == s1:  
   print("yes")  
else:  
   print("no")
