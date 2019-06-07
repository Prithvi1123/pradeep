a = input()
b=0
c=0
for i in range(len(a)):
    if(a[i].isalpha() or a[i].isdigit()):
       b=b+1
    else:
        c=c+1
print(c)
