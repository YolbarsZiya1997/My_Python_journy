def fizz_buzz(jawap: int) -> str:
    """the fizz_buzz game:
      if you enter a number that is divisible by 3, the function
    gives you back the answer "fizz"
      if you enter a number that is divisible by 5, the function
    gives you back the answer "buzz"
      lastly, if you enter a number that is both divisible by 3 and 5
    the function returns the answer "fizz buzz"

    Args:
        jawap (int): your input

    Returns:
        str: returns the strings "fizz","buzz", and "fizz buzz"
    """
    if jawap % 3 == 0 and jawap % 5 == 0:
        resultt = "fizz buzz"
        return resultt
    elif jawap % 5 == 0:
        results = "buzz"
        return results
    elif jawap % 3 == 0:
        result = "fizz"
        return result
    else:
        return str(jawap)
    

input("Play Fizz Buzz.  Press ENTER to start")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("Your go:")
    # players_answer = correct_answer
    if players_answer != correct_answer:
        print("You lose, the correct answer was {}".format(correct_answer))
        break

else:
    print("Well done, you reached {}".format(next_number))
    
