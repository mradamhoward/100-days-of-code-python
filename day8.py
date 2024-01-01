# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


# def greet():
#     print("Hello World!")
#     print("Hello World!")
#     print("Hello World!")
#
#
# greet()

# def greet_with_name(name):
#     print("Hello " + name)
#
# greet_with_name("Adam")

# def greet_with(name, location):
#     print(f"Hello {name} your location is {location}")
#
# greet_with("Adam", "Cobh")
import math
def paint_calc(height, width, cover):
    cans = (width * height) / cover
    round_up_cans = math.ceil(cans)
    print(f"You'll need {round_up_cans} cans of paint. ")
test_h = 4
test_w = 5
coverage = 5
paint_calc(test_h, test_w, coverage)

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    return is_prime

n = 11
print("Is " + str(n) + " Prime: " + str(prime_checker(n)))