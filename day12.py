import random


EASY_NUM_GUESSES  = 10
HARD_NUM_GUESSES = 5

correct_value = random.randint(1,100)

guesses = 0

print("Welcome to the Number Guessing Game! ")
print("I'm thinking of a number between 1 and 100. it is " + str(correct_value))

easy_or_hard = input("Choose a difficulty. easy or hard: ")

if easy_or_hard == 'easy':
    guesses = EASY_NUM_GUESSES
else:
    guesses = HARD_NUM_GUESSES

while guesses != 0:
    guess = int(input("Make a guess: "))
    if guess < correct_value:
        print("Too low")
        print("Guess again")
    elif guess > correct_value:
        print("Too high")
        print("Guess again")
    elif guess == correct_value:
        print("Correct")
        print("Well done!")
        break
    guesses -= 1
    print(f"You have {guesses} remaining.")

print(f"The number was {correct_value}")

