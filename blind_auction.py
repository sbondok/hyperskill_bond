
blind_auction = {}

end_bid = False
while not end_bid:
    name = input("Enter your name: \n")
    bid = int(input("Enter your bid: $"))

    blind_auction[name] = bid
    end = input("Another bidder? (y/n) ").lower()
    if end == "n":
        end_bid = True


max_bid = 0
winner = ''
for key in blind_auction:
    if blind_auction[key] > max_bid:
        max_bid = blind_auction[key]
        winner = key

print(f"The winner is {winner} with auction ${max_bid}")

