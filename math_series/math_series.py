from re import X


def fibonacci(num):
    """Return the nth number in the Fibonacci series."""
    if type(num) != int:
        return "Please Enter a Number"
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

def lucas(num):
    """Return the nth number in the Lucas series."""
    if type(num) != int:
        return "Please Enter a Number"
    if num==0:
        return 2
    elif num==1:
        return 1
    else:
        return lucas(num-1) + lucas(num-2)


def sum(num,x=0,y=1):
    """Return the nth number in a series where the user decides the base arguments.
    If the optional arguments were not specified the function returns the nth number in the Fibonacci series."""
    if type(num) != int:
        return "Please Enter a Number"
    if num == 0:
        return x
    elif num == 1:
        return y
    else:
        return sum(num-1,x,y) + sum(num-2,x,y)