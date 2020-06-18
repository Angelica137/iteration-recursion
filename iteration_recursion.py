def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    number = 1
    if exp == 0:
        return number
    else:
        for i in range(exp):
            number *= base
    return number


print(iterPower(6.62, 7))
