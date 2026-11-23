# https://github.com/hedychia/lab11-HM-KK.git
# Partner 1: Haiden Machado
# Partner 2: Kai Kim


"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math 

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
def square_root(a):
    try: 
        if a<0:
            raise ValueError("Cannot take square root of a negative number")
        return math.sqrt(a)
    except ValueError:
        raise

def hypotenuse(a, b):
    try:
        return math.sqrt((a*a)+ (b*b))
    except Exception:
     raise

# First example

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError('division by zero')
    return a / b

def logarithm(a, b):
    if a<= 0 or a ==1 or b <= 0:
        raise ValueError("Invalid base for logarithm")
    return math.log(b, a)

def exp(a, b):
    return a**b
    return a + b


