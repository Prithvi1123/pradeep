num=int(input(" "))
num1=0
num2=1
for i in range(0,num):
    print(num2,end=" ")
    num3=num1+num2
    num1=num2
    num2=num3
