class Shape:
    def __init__(self,type):
        self.type=type
class Circle(Shape):
    def __init__(self,type,radius):
        super().__init__(type)
        self.radius=radius
    def getArea(self):
        print(f"The type of shape is {self.type}")
        print(f"The radius is {3.14*self.radius*self.radius}")
class Square(Shape):
    def __init__(self,type,length,breadth):
        super().__init__(type)
        self.length=length
        self.breadth=breadth
    def getArea(self):
        print(f"The shape is {self.type}")
        print(f"The area is {self.length*self.breadth}")
class Triangle(Shape):
    def __init__(self,type,base,height):
        super().__init__(type)
        self.base=base
        self.height=height
    def getArea(self):
        print(f"The type of shape is {self.type}")
        print(f"The area is {0.5*self.base*self.height}")
obj1=Circle('Circle',2)
obj2=Square('Square',4,5)
obj3=Triangle('Triangle',2,4)
obj1.getArea()
obj2.getArea()
obj3.getArea()


