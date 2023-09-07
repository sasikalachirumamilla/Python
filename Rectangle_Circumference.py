class Rectangle:
    pi=3.14
    def __init__(self,length=5,breadth=5):
        self.length=length
        self.breadth=breadth
    def circumference(self):
        return (2*(self.length+self.breadth))
Rectangle_1=Rectangle(2,2)
print(Rectangle_1.circumference())
Rectangle_2=Rectangle(3,2)
print(Rectangle_2.circumference())
Rectangle_3=Rectangle() #Declared the values in function
print(Rectangle_3.circumference())