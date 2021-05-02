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
    

for i in range(101):
    print(fizz_buzz(i))
    
    
