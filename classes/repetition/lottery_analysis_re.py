from random import choice 

def get_winning_tickets(possibilities):
    """ Return a winning ticket from a list of possibilities"""
    
    
    winning_ticket = []
    
    # We don't want the content of the winning ticket to repeat
    # thus we are gonna use a while loop
    
    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)
            
    return winning_ticket

def check_ticket(played_ticket, winning_ticket):
    # check all the content of the played_ticket if any of it 
    # not in the winning ticket return false
    
    for item in played_ticket:
        if item not in winning_ticket:
            return False
    
    # for the winning ticket    
    return True

def ticket_maker(possibilities):
    """ random ticket generator """
    
    
    played_ticket = []
    
    while len(played_ticket) < 4:
        pulled_item = choice(possibilities)
        if pulled_item not in played_ticket:
            played_ticket.append(pulled_item)
            
    return played_ticket


possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = get_winning_tickets(possibilities)

plays = 0
won = False

max_tries = 1_000_000

while not won:
    new_ticket = ticket_maker(possibilities)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break
    
if won:
    print('We have a winning ticket')
    print(f'Your ticket is {new_ticket}')
    print(f'The winning ticket is {winning_ticket}')
    print(f'It took {plays} tries to won')
    
else:
    print(f'Tried {plays} times without a winner')
    print(f'Your ticket {new_ticket}')
    print(f'Winning ticket {winning_ticket}')
        