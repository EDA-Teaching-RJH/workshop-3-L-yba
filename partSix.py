age = int(input("What is your age?"))
student = input("Are you a student? (yes/no): ")

if age<12 or age>=65:
   print("you pay £5")
elif 12<=age<=64 and student== "yes"   :
 print("you pay £8")
else:
   print("you pay £10")
   