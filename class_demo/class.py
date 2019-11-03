from class_demo.my_class import *
from class_demo.classTwo import *

obA = MyFirstClass()
obA.setData('abc')
obA.details()

obB = MyFirstClass()
obB.setData(123)
obB.details()

rectangleA = Rectangle(3, 4)
rectangleB = Rectangle(5, 6)

print("Area of \"rectangleA\" is %d and area of \"rectangleB\" is %d." % (rectangleA.area(), rectangleB.area()))
