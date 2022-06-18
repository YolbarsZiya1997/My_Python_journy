from random import choice

possibility = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

# Now we need to have a list for the winning ticket
winning_ticket = []

# Since the content of the ticlet are not repeating
# we need a while loop

print("Now let's see what we got...")
while len(winning_ticket) < 4:
    pulled_item = choice(possibility)
    
    if pulled_item not in winning_ticket:
        winning_ticket.append(pulled_item)
        

for item in winning_ticket:
    print(f'We have a {item}')
        
# and finally
print(f"The winner is {winning_ticket}")