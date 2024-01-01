print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? €"))
percentage_tip = int(input("What percentage tip would you like to give? 10%, 12%, or 15%: "))
num_split_bill = int(input("How many people to split the bill? "))

total = round((bill * (1 + (percentage_tip / 100))) / num_split_bill, 2)

print(f"Each person should pay: €{total}")