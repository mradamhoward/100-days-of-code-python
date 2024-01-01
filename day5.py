# students_height = input().split()
# total = 0
# for n in range(0, len(students_height)):
#     students_height[n] = int(students_height[n])
#     total += students_height[n]
#
# average = total / len(students_height)
#
# print(average)

scores = [78, 65, 89, 86, 55, 91, 64, 89]

highest_score = 0

for score in scores:
    if score > highest_score:
        highest_score = score

print("The max score is: " + str(highest_score))


total = 0
for n in range(0, 101):
    total += n

print(f"The total is {total}")

even_limit = int(input("Enter a number: "))

total_even = 0

for even in range(0, even_limit + 1, 2):
    total_even += even

print(f"The total of even numbers is {total_even}")

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)