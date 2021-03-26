# Closure in python: The data 'msg' gets attached with code
def print_msg(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested function
        print(msg)

    return printer  # returns the nested function


# Now let's try calling this function.
# Output: Hello
another = print_msg("Hello") # function 'printer' is returned that has access to non-local variable
another()       # returned function is called

# you can delete the function
del print_msg
another()       # the function 'print_msg' remains in ram only for the attatched variable 'another'

print_msg('hi') # it will generate an error as print_msg function is deleted, however it can be accessed using 'another' refernce
del another     # reference is also deleted
another()       # error, as reference and referenced function both are deleted