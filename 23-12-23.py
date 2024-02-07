# # 1
# class india:
#     def __init__(self,population,chiefminister,business,networth,tourist):
#         self.population=population
#         self.cm =chiefminister
#         self.business=business
#         self.networth=networth
#         self.tourist=tourist
#     def states(self):
#         print("population is:",self.population)
#         print("Cm is:",self.cm)
#         print("business sector is",self.business)
#         print("networth :",self.networth)
#         print("tourist places",self.tourist)    
# class Telangana(india):
#     def __init__(self,population,business,networth,tourist,ITsector,famousfor):
#         super().__init__(population,chiefminister,business,networth,tourist)
#         self.ITsector=ITsector
#         self.famousfor=famousfor
#     def m1(self):
#         super().states()
#         print("ITsector consists of",self.ITsector)
#         print("famous for",self.famousfor)
# class Andhra_pradesh(india):
#     def __init__(self,population,business,networth,tourist,beach,temples):
#         super().__init__(population,chiefminister,business,networth,tourist)
#         self.beach=beach
#         self.temples=temples
#     def m2(self):
#         super().states()
#         print("beach :",self.beach)
#         print("temples:",self.temples)
# e1=Telangana("35,003,674","Revanth Reddy","finance,investment,healthcare,","83.4 billion","Charrminar","Thub","startup companies")          
# e1.m1()
# print()
# s1=Andhra_pradesh("9.46 crores","Jagan","finance,investment,healthcare,","83.4 billion","Araku","vizag beach","tirupathi") 
# s1.m2()
# print()


# # 2 
# import math
# class Shape:
#     def area(self):
#         pass
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return math.pi * self.radius**2
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length * self.width
# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#     def area(self):
#         return 0.5 * self.base * self.height
# if __name__ == "__main__":
#     circle_radius = 5
#     circle = Circle(circle_radius)
#     print(f"Area of the circle with radius {circle_radius}: {circle.area()}")
#     rectangle_length = 4
#     rectangle_width = 6
#     rectangle = Rectangle(rectangle_length, rectangle_width)
#     print(f"Area of the rectangle with length {rectangle_length} and width {rectangle_width}: {rectangle.area()}")
#     triangle_base = 3
#     triangle_height = 8
#     triangle = Triangle(triangle_base, triangle_height)
#     print(f"Area of the triangle with base {triangle_base} and height {triangle_height}: {triangle.area()}")


# 3
# Single Inheritance
class Parent:
    def __init__(self):
        print("Parent class constructor")
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child class constructor")
# Multiple Inheritance
class A:
    def __init__(self):
        print("Class A constructor")
class B:
    def __init__(self):
        print("Class B constructor")
class C(A, B):
    def __init__(self):
        super().__init__()
        super(B, self).__init__()  
        print("Class C constructor")
# multilevel Inheritance
class Grandparent:
    def __init__(self):
        print("Grandparent class constructor")
class Parent(Grandparent):
    def __init__(self):
        super().__init__()
        
        print("Parent class constructor")
class Child(Parent):
    def __init__(self):
        super().__init__()  # Calls the constructor of Parent class
        print("Child class constructor")
if __name__ == "__main__":
    print("Single Inheritance:")
    obj_child = Child()
    print("\nMultiple Inheritance:")
    obj_c = C()
    print("\nMultilevel Inheritance:")
    obj_grandchild = Child()

