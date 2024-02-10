import random
words = ['Melanie', 'Georgia', 'Hayden', 'Zara', 'Wendy', 'Darren', 'Valerie']
secret_word = random.choice(words)
num_guesses = 0
while True:
    guess = input("guess the secret name ")
    num_guesses += 1
    if guess == secret_word:
        print("congrats, you got the secret word in", num_guesses, "guesses")
        break
    elif num_guesses == 3:
        print("sorry you have run out of guesses, the secret word is", secret_word)
        break
    else:
        print("incorrect, guess again.")