print("Welcome to Treasure Island.")

choice1 = input("You are at a crossroad, where do you go? left or right? ").lower()



if choice1 == "left":
    choice2 = input("You've come to a lake. There is an island in the middle of the lake. Type wait or swim.").lower()
    if choice2 == "wait":
        choice3 = print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
        if choice3 == "red":
            print("Game over.")
        elif choice3 == "yellow":
            print("You win.")
        elif choice3 == "blue":
            print("Game over.")
        else:
            print("Game over.")
    else:
        print("Game over.")
else:
    print("Game over.")






print("The Love Calculator is calculating your score...")
name = input("What is the first naem? ")
name2 = input("What is the second name? ")

combined_names = name + name2
lowered_names = combined_names.lower()

t = lowered_names.count("t")
r = lowered_names.count("r")
u = lowered_names.count("u")
e = lowered_names.count("e")

first_digit = t + r + u + e

l = lowered_names.count("l")
o = lowered_names.count("o")
v = lowered_names.count("v")
e = lowered_names.count("e")

second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")




#Exercise 2
height = float(input("Enter your height in meters: "))
weight = int(input("Enter your weight in kgs: "))

bmi = weight / (height * height)

if bmi < 18.5:
    print(f"You are underweight. Your BMI is: {bmi}")
elif bmi < 25:
    print(f"You are a normal weight. Your BMI is: {bmi}")
elif bmi < 30:
    print(f"You are slightly overweight. Your BMI is: {bmi}")
elif bmi < 35:
    print(f"You are obese. Your BMI is: {bmi}")
else:
    print("You are morbidly obese. Your BMI is: {bmi}")

#Exercise 3
print("Welcome to Portaventura Dragon Khan")
height = int(input("What is your height in cm?: "))

if height >=120:
    print("You can ride.")
    age = int(input("What is your age?: "))
    if age >= 18:
        print("It costs €10")
    elif age < 18 and age >= 12:
        print("It costs €7")
    else:
        print("It costs €5")
else:
    print("Sorry you can't ride.")