"""
Write a function recurPower(base, exp) which computes  by recursively calling itself to solve a smaller version of the same problem, and then multiplying the result by base to solve the initial problem.

This function should take in two values - base can be a float or an integer; exp will be an integer . It should return one numerical value. 
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # when exp == 1, base^exp = base
    if exp <= 0:
        return 1
    return base * recurPower(base, exp-1)