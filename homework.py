# program that converts Celsius to Fahrenheit
celsius = float(input("temperature in celsius: "))
fahrenheit = celsius * 1.8 + 32
print("the temperature is fahrenheit is", fahrenheit)

# program to calculate age
birthyear = float(input("what is your birth year: "))
currentyear = 2023
age = currentyear - birthyear
print("you are", age, "year(s) old.")

# program to check if number is positive or negative
integer = (float(input("enter your number: ")))
if integer < 0:
    print("negative number")
elif integer > 0:
    print("positive number")
elif integer == 0:
    print("0 is neither negative nor positive!")

# program to check if a number is even or odd
number = (float(input("enter your number: ")))
if number % 2 == 0:
    print("even number")
else:
    print("odd number")