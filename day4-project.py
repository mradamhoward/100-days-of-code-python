import random

choice = input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors? ")

computer_choice = random.randint(0, 2)

choice = int(choice)

print("Computer chose: " + str(computer_choice))

if choice == 0 and computer_choice == 2:
    print("You win")
elif choice == 1 and computer_choice == 0:
    print("You win")
elif choice == 2 and computer_choice == 1:
    print("You win")
elif choice == 0 and computer_choice == 0:
    print("Draw")
elif choice == 1 and computer_choice == 1:
    print("Draw")
elif choice == 2 and computer_choice == 2:
    print("Draw")
else:
    print("You lose")