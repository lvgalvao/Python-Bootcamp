from replit import clear
from artlogo import logo

print(logo)
print("Welcome to the bid system")

bids = {}
bidding_finished = False

def find_highest_biddder(bidden_record):
    highest_bidder = 0
    winner = ""
    for bidder in bidden_record:
        bid_amound = bidden_record[bidder]
        if bid_amound > highest_bidder:
            highest_bidder = bid_amound
            winner = bidder
    print(f"The winner is {winner} with the bid {highest_bidder}")

while not bidding_finished:
    name = str(input("What is your name? "))
    offer = int(input("What is your offer? $"))
    bids[name] = offer
    keep_bidding = input("Do you want to place other bid? ")
    if keep_bidding == "no":
        bidding_finished = True
        find_highest_biddder(bids)
    else:
        clear()
