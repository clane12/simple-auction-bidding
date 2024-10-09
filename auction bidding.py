import random
import art
lis = [1,2,3,4,5,6,7,8,9,10]
bidding = True

print(art.logo)

print("\n bidding starts: -------------")
bidders = {}
while bidding:
    name = input("What is your Name?: ")
    bid = int(input("How much would you like to bid?: "))

    bidders[name + str(random.choice(lis))] = bid # to avoid the repetition of the same name.


    again = True
    while again:
        more = input("Are there others who would like to bid, say 'yes' or 'no' ").lower()
        if more == "yes":
            print("\n" * 100)
            break
        elif more == "no":
            bidding = False
            break
        else:
            print("you typed something wrong, try again")

# to find the highest number in the dictionary
finalbid = 0
finalbidder = ""
final = {}
for bidder in bidders:
    if finalbid < bidders[bidder]:
        finalbid = bidders[bidder]
        finalbidder = bidder

final[finalbidder] = finalbid

print(final)



# to find the highest in the dictionary it can also be written as
# print(max(bidders, key=bidders.get))

