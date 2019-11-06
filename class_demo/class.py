from class_demo.my_class import MyFirstClass
from class_demo.classTwo import Rectangle


def objectA():
    obA = MyFirstClass()
    obA.setData('abc')
    obA.details()
    pass


def objectB():
    obB = MyFirstClass()
    obB.setData(123)
    obB.details()
    pass


rectangleA = Rectangle(3, 4)
rectangleB = Rectangle(5, 6)

print("Area of \"rectangleA\" is %d and area of \"rectangleB\" is %d." % (rectangleA.area(), rectangleB.area()))
