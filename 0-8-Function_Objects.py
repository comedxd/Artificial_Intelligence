"""
In python everyting is an object either variables or functions
A function object can be given different names
"""
def first(msg):
    print(msg)


first("Hello python")

second = first      # function is assigned to a variable, the names first and second refer to the same function object.
second("Hello")
#====================================================================================================================
# Decorators are part of a larger subject called meta programming.
# Decorators are functions that take your function as an input.
# The idea is to encode reusable functionality as decorator functions and then decorate other functions with it.
# The purpose is to give your function a feature it didn't have before.
# A decorator can, for example, add fields to your object, measure the time it takes to invocate a function, and do much more.

# The @property decorator does the following things for you:
    # Creates a backing field: When you decorate a function with the @property decorator,
        # it creates a backing private field. You can override this behavior if you want, but it's nice to have a default behavior.
    # Identifies a setter: A setter method can change the backing field.
    # Identifies a getter: This function should return the backing field.
    # Identifies a delete function: This function can delete the field.
#===================================================================================================================
"""
class Square:
    def __init__(self, w, h):
        self.height = h     # public variable
        self.__width = w    # private variable

    def set_side(self, new_side):
        self.__height = new_side
        self.__width = new_side

    @property
    def area(self):
        return self.__area    # a new field is created which is not defined in constructor

    @area.setter
    def area(self, new_value):
        if new_value >= 0:
            self.__area = new_value
        else:
            raise Exception("Value must be larger than 0")

sq=Square(2,2)
print(sq.area)
"""