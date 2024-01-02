import art
import game_data
import random

data = game_data.data

print(art.logo)

score = 0

while True:
    print("-----------------------")

    random_a = data[random.randint(0, len(data) - 1)]
    random_b = data[random.randint(0, len(data) - 1)]

    print("Compare A: " + random_a["name"] + ", " + random_a["description"] + ' from ' + random_a["country"])
    print(art.vs)
    print("Compare B: " + random_b["name"] + ", " + random_b["description"] + ' from ' + random_b["country"])

    guess = input("Who has more followers? Type A or B: ").lower()

    correct_answer = ""

    if random_a["follower_count"] > random_b["follower_count"]:
        correct_answer = "a"
    else:
        correct_answer = "b"

    if guess == correct_answer:
        score += 1
        print("Correct! " + random_a["name"] + " has "+ str(random_a["follower_count"]) + " followers.")
        print(random_b["name"] + " has " + str(random_b["follower_count"]) + " followers.")
        print(f"Your score is {score}.")
    else:
        print("Incorrect! " + random_a["name"] + " has " + str(random_a["follower_count"]) + " followers.")
        print(random_b["name"] + " has " + str(random_b["follower_count"]) + " followers.")
        print("Game over...")
        print(f"Your final score is {score}.")
        break