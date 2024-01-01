import random
import my_module
random_integer = random.randint(1,10)
print(random_integer)

random_float = random.random() * 5
print(random_float)

print(my_module.pi)

heads_or_tails = random.randint(0, 1)

if heads_or_tails == 1:
    print("Heads")
else:
    print("Tails")

states_of_america = ['Delaware', 'Pennsylvania', 'New Jersey', 'Georgia', 'Connecticut', 'Massachusetts', 'Maryland', 'South Carolina', 'New Hampshire', 'Virginia', 'New York', 'North Carolina', 'Rhode Island', 'Vermont', 'Kentucky', 'Tennessee', 'Ohio', 'Louisiana', 'Indiana', 'Mississippi', 'Illinois', 'Alabama', 'Maine', 'Missouri', 'Arkansas', 'Michigan', 'Florida', 'Texas', 'Iowa', 'Wisconsin', 'California', 'Minnesota', 'Oregon', 'Kansas', 'West Virginia', 'Nevada', 'Nebraska', 'Colorado', 'North Dakota', 'South Dakota', 'Montana', 'Washington', 'Idaho', 'Wyoming', 'Utah', 'Oklahoma', 'New Mexico', 'Arizona', 'Alaska', 'Hawaii']


print(states_of_america)

names = input().split(", ")

random_index = random.randint(0, len(names) - 1)
print(names[random_index] + " is paying today.")

line1 = ["","",""]
line2 = ["","",""]
line3 = ["","",""]

map = [line1,line2,line3]
print("Hiding your treasure, X marks the spot.")
position = input()

letter = position[0].lower()
abc = ["a", "b", "c"]

letter_index = abc.index(letter)
number_index = int(position[1]) - 1

map[number_index][letter_index] = 'X'

print(f"{line1}\n{line2}\n{line3}")