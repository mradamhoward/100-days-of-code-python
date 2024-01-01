bids = {}
finished = False

def find_highest_bidder(record):
    highest_bid = 0
    winner = ""
    for bidder in record:
        amount = record[bidder]
        if amount > highest_bid:
            highest_bid = amount
            winner = bidder
    print(f"The winner is {winner} with bid of €{highest_bid:.2f}")


while not finished:
    name = input("What is your name? ")
    price = float(input("What is your bid? €"))
    bids[name] = price
    answer = input("Are there any other bidders? type yes or no: ")
    if answer == "no":
        finished = True
        find_highest_bidder(bids)