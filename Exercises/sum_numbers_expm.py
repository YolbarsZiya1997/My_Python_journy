def sum_numbers(*numbers: float) -> float:
    """function summs the numbers you enter
    Args:
        float: the inputs to be summed
    Returns:
        float: the result
    """
    summation = 0
    for i in numbers:
        summation += i
    return summation


