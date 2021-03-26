# Functions can be passed as arguments to another function
# higher order functions: the functions that take other functions as parameters

def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operate(func, x):
    result = func(x)
    return result

# Driver Code
print(operate(inc,5))
print(operate(dec,10))