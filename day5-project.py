import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

type = random.randint(0, 2)

password = ''

while nr_numbers > 0 or nr_symbols > 0 or nr_letters > 0:
    type = random.randint(0, 2)
    if type == 0:
        if nr_letters > 0:
            password += letters[random.randint(0, len(letters)- 1)]
            nr_letters -= 1
    elif type == 1:
        if nr_symbols > 0:
            password += symbols[random.randint(0, len(symbols) - 1)]
            nr_symbols -= 1
    elif type == 2:
        if nr_numbers > 0:
            password += numbers[random.randint(0, len(numbers)- 1)]
            nr_numbers -= 1

password_list = list(password)

print("Before shuffle: " + password)

random.shuffle(password_list)

password = ''.join(password_list)
print("After shuffle: "+ password)