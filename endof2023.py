StuName = input("what is your name? ")
StuAge = float(input("How old are you? "))
StuCol = input("What is your favourite colour? ")
print("hello", StuName, "your favourite colour is ", StuCol)

numa = 5
numb = 3
numc = numa * numb
print(numc)

yes = 17 % 5
print(yes)

num = float(input("give a number: "))
if num < 20 and num > 10:
    print("yes")
else:
    print("no")

numone = float(input("what is the first number: "))
numtwo = float(input("what is the second number: "))
summ = numone + numtwo
difference = numone - numtwo
product = numone * numtwo
quotient = numone / numtwo
print("The sum is", summ)
print("The difference is", difference)
print("The product is", product)
print("The quotient is", quotient)

age = float(input("How old are you?"))
if age > 18:
    print("you are old enough to vote!")
elif age < 18:
    print("You are too young to vote!")
elif age < 13 and age > 6:
    print("You are too young to vote! You are still in elementary school!")\

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in numbers:
    print(x)

while True:
    guess = float(input("guess a number: "))
    if guess > 5:
        print("your guess is valid, as it is greater than 5!")
        break
    else:
        print("incorrect, guess again.")

Studentnames = ['Melanie', 'Georgia', 'Hayden', 'Zara', 'Wendy']
for x in Studentnames:
    print(x.upper())

