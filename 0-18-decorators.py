def make_pretty(func):
    print("it is outer function")
    def thecaller():
        print("I got decorated")
        func()                      # calling the passed function
    return thecaller


"""
def ordinary():
    print("I am ordinary")

pretty = make_pretty(ordinary)
pretty()
ordinary=make_pretty(ordinary) 
ordinary()
# commented code is equivalent to following code                     
"""
@make_pretty
def ordinary():
    print("I am ordinary")
ordinary()
