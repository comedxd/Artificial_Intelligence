class Square:
    def __init__(self):
      self._height = 2
      self._width = 2
    def set_side(self,new_side):
      self._height = new_side # variables having name starting with _ are called protected variables
      self._width = new_side # protected variable can be accessed outside class

square = Square()
square._height = 3 # not a square anymore
print(square._height,square._width)