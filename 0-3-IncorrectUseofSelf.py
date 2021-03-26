class Car:
  def __init__():  # must pass self object
    self.color = "Red" # ends up on the object
    make = "Mercedes" # becomes a local variable in the constructor

car = Car()
print(car.color) # "Red"
print(car.make) # would result in an error, `make` does not exist on the object