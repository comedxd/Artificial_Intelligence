# we can make general decorators that work with any number of parameters
# In Python, this magic is done as function(*args, **kwargs).
# In this way, args will be the tuple of positional arguments and kwargs will be
# the dictionary of keyword arguments.
# An example of such a decorator will be:

def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star               # star decorates (covers) the percent function
@percent            # percent function decorates (covers) the printer function
def printer(msg):
    print(msg)


printer("Hello")    # printer object points to object of percent that further points to star object.
                    # 'star' prints stars and then calls the 'precent' function that prints the '%'
                    # then line 18 is executed to call the printer function to print 'hello'
                    # then line of % is printed
                    # finally a line of * is printed