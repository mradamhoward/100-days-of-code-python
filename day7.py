import random
#Step 1

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = word_list[random.randint(0, len(word_list)-1)]
print("Chosen word: " + chosen_word)

blanks = []
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

for letter in chosen_word:
    blanks.append("_")

def does_blanks_contain_underscore():
    for letter in blanks:
        if letter == "_":
            return True

    return False

lives = 6

while does_blanks_contain_underscore():
    if lives == 0:
        print("You lose")
        break

    guess = input("Guess a letter: ").lower()

    print(stages[lives])

    blanks_index = 0


    for letter in chosen_word:
        if letter == guess:
            blanks[blanks_index] = letter
        blanks_index += 1

    if guess not in chosen_word:
        lives -= 1


    print("lives: " + str(lives))
    print(blanks)

