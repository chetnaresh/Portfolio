class Shape:
    def getArea(self):
        print("Different Forms of Shape")
class Circle(Shape):
    def getArea(self):
        radius=int(input("enter the radius"))
        res=3.14*radius*radius
        print(res)
class Square(Shape):
    def getArea(self):
        length=int(input("enter the length"))
        breadth=int(input("enter the breadth"))
        res=length*breadth
        print(res)
class Triangle(Shape):
    def getArea(self):
        base=int(input("enter the base value "))
        height=int(input("enter the height"))
        res=0.5*base*height
        print(res)
c=Circle()
s=Square()
t=Triangle()

c.getArea()
s.getArea()
t.getArea()