#create a compare list

from artday14 import logo, vs
from datagameday14 import data
import random

def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_descr}, from {account_country}")

#diaplay art

print(logo)

#generate a ranom account from the game data

account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)

print(f"Compare A: {format_data(account_a)}.")
print(vs)
print(f"Compare B: {format_data(account_b)}.")


guess = input("Who has more followers? Type 'A' or 'B'").lower

a_follower_count = account_a["follower_count"]
b_follower_count = account_b["follower_count"]



#format the account data into printable format

#ask a user for a guess

#check if user is correct
## get follower count of each account
## use if statament to check if user is correct

#give user feedback on ther guess

#make the game repeatable

# making account at position b become the next account at position a

#clear the scream between rounds

