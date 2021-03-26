def is_called():
    def is_returned():
        print("Hello")
    return is_returned # function is being returned

x = is_called()

# Outputs "Hello"
x() # calling function "is_called" referenced by x