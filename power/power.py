def power_num(number: float, power: int) -> float:
    """
    Raise the number to the power if number >= 0.
    """
    #the number can be int or float
    if not isinstance(number, int) and not isinstance(number, float):
        raise TypeError ("the number can only be int or float")

    #the power can only be int
    if not isinstance(power, int):
        raise TypeError("the power can only be in int type")

    #if number > 0, we compute the calculation
    if number >= 0:
        return round(number ** power, 2)
    raise TypeError("The number can only be >= 0")