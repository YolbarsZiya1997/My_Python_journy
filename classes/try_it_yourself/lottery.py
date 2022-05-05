""" Make a list or tuple containing a series of 1o numbers and five letters. Randomly 
select four numbers or letters from the list and print a message saying that any ticket
matching these four numbers or letters wins a prize"""

from random import choice

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

winning_tickets = []
print("Let's see what the winning_tickets is...")

# We don't want to repeat winning numbers or letters, we'll use a 
# while loop.

while len(winning_tickets) < 4:
    pulled_item = choice(possibilities)
    
    # only add the pulled item to the winning_tickets if it hasn't
    # already been pulled 
    if pulled_item not in winning_tickets:
        winning_tickets.append(pulled_item)
        print(f"We pulled a {pulled_item}!")
          