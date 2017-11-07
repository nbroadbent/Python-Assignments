# Family name: Nicholas Broadbent
# Student number:  8709720
# Course: IT1 1120 
# Assignment Number 5

def digit_sum(n):
    ''' (int)->int

    This function returns the sum of all of the digits
    of the integer n.
    '''
    
    if n > 0:
        # Take the last number, remove it and add it
        x = n/10
        n = n//10
        return digit_sum(n) + round((x-n)*10)
    return 0

def digital_root(n):
    ''' (int)->int

    Returns the sum of the sum of digits of an integer n,
    or the digital roots of integer n.
    '''
    
    # Get sum of digits
    n = digit_sum(n)

    # Get digital root
    if n > 10:
        return digital_root(n)
    return n
