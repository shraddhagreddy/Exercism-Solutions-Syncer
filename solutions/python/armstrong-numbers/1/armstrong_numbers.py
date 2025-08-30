def is_armstrong_number(number):
    """An Armstrong number is a number that is the sum of its own digits each raised to        : the power of the number of digits."""
    original=number
    count=0
    n=number
    while n>0:
        n=n//10
        count=count+1
    total=0
    n=number
    while n>0:
        digit=n%10
        total+=digit**count
        n=n//10

    return total==original
        