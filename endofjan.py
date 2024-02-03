numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in numbers:
    print(x)

num1 = float(input("what is the first number? "))
num2 = float(input("what is the second number? "))
if num1 > num2:
    print("the bigger number is", num1)
elif num2 > num1:
    print("the bigger number is", num2)
else:
    print("the numbers are the same")

x = 0
while x <= 19:
    x += 2
    print (x)

name = "anjelina"
for i, v in enumerate(name):
    print(v)
