grade = int(input("what is your grade between 0-100"))
if grade < 0 or grade > 100:
   print("Invalid age. Please enter a value between 0 and 120.")

if 90<=grade<=100:
   print("A")
elif 80<=grade<=89:
   print("B")
elif 70<=grade<=79:
   print("C")
elif 60<=grade<=69:
   print("D")
elif grade<60:
   print("FAIL")

