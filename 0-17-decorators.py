def make_pretty(func):
    print("it is outer function")
    def thecaller():
        print("I got decorated")
        func()                      # calling the passed function
    return thecaller


def ordinary():
    print("I am ordinary")

#pretty = make_pretty(ordinary)
#pretty()
ordinary=make_pretty(ordinary) # now identifier 'ordinary' points to a different object 'thecaller', not to function ordinary.
ordinary()                      # calling new ordinary will now actually call 'thecaller' and 'thecaller' will call the 'old' ordinary