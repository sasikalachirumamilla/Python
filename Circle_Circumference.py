class Circle:
    pi=3.14
    def __init__(self,r):
        self.radius=r
    def circumference(self):
        return 2*Circle.pi*self.radius
Circle_1=Circle(4) #passing the radius
print(Circle_1.circumference())

Circle_2=Circle(5)
print(Circle_2.circumference())