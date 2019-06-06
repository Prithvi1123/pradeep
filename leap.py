yr = int(input("Enter a year: "))
if (yr % 4) == 0:
   if (yr % 100) == 0:
       if (yr % 400) == 0:
           print("yes")
       else:
           print("no")
   else:
       print("yes")
else:
   print("no")
