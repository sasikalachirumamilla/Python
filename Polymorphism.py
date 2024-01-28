class Car:
  def __init__(self, brand, model, age):
    self.brand = brand
    self.model = model
    self.age=age

  def move(self):
    print("Polymorphism")

class Boat:
  def __init__(self, brand, model,age):
    self.brand = brand
    self.model = model
    self.age=age

  def move(self):
    print("Polymorphism1")

class Plane:
  def __init__(self, brand, model,age):
    self.brand = brand
    self.model = model
    self.age=age

  def move(self):
    print("polymorphism2")

car1 = Car("h", "i",20)       #Create a Car class
boat1 = Boat("python", "class",30) #Create a Boat class
plane1 = Plane("method", "object",40)     #Create a Plane class

for x in (car1, boat1, plane1):

	print(x.brand)
	print(x.model)
	print(x.age)
	x.move()