def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations  = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number? "))

for operation in operations:
    print(operation)

operation_symbol = input("Pick an operation from the line above: ")

operation = operations[operation_symbol]
result = operation(num1, num2)
print(f"Result of {num1} {operation_symbol} {num2} = {result}")

while True:
    keep_going = input("Do you want to continue? Y or N: ").lower()
    if keep_going == 'n':
        break
    operation_symbol = input("Pick another operation: ")
    num3 = int(input("Whats the next number? "))
    operation = operations[operation_symbol]
    second_result = operation(result, num3)

    print(f"Result of {result} {operation_symbol} {num3} = {second_result}")
    result = second_result