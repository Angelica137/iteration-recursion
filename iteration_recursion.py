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


def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        return base*recurPower(base, exp - 1)


print(recurPower(3, 0))
