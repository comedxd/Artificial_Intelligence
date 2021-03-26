# Defining the nested function only
def print_msg(msg):
    def printer():
        print(msg)  #nested function is accessing the non-local variable 'msg'
    printer()
    print("i am outer function")
    printer() # calling the nested function

# driver code
print_msg("this is message")