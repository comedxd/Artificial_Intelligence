# Defining the nested function only
def print_msg():
    def printer():
        # This is the nested function
        print("I am nested function")
    print("i am outer function")

# driver code
print_msg()
