num = int(input("Enter a number: "))
base = 1
if num < 0:
   print("Sorry, factorial does not exist")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for n in range(1,num + 1):
       base = base*n
   print("The factorial of",num,"is",base)