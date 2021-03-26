def make_pretty(func):
    print("it is outer function")
    def thecaller():
        print("I got decorated")
        func()                      # calling the passed function
    return thecaller


def ordinary():
    print("I am ordinary")

# driver code
ordinary()

pretty = make_pretty(ordinary) # a function is passed to other function, 'make_pretty' is decorator and 'thecaller' is decorated
pretty()                        # calling the returned function i.e. 'thecaller' function