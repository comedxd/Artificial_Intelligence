class Square:
    def __init__(self):
      self.__height = 2
      self.__width = 2
    def set_side(self,new_side):
      self.__height = new_side
      self.__width = new_side

square = Square()
#print(square.__height) # raises AttributeError
square.__height = 3
print(square.__height)