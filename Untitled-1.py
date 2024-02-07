# #6
# from random import *
# for i in range(100):
#     print(randint(6000000000,9000000000)) 

# # 1
# import math
# print(dir(math)) 

# # 5
# import random
# print(dir(random))

# # 3
# a = int(input("Enter the number: "))
# b = int(input("Enter the number: "))

# print("operation 1:")
# z = pow(a,2)+pow(b,2)+2*a*b
# print("(a+b)^2 = ",z)

# print("operation 2 :")
# y = pow(a,2)-pow(b,2)-2*a*b
# print("(a-b)^2",y)

# print("operation 3 :")
# x = pow(a,3)+pow(b,3)+3*pow(a,2)*b+3*a*pow(b,2)
# print("(a+b)^3",x)

# # 4
# import math
# r = int(input("Enter the radius: "))
# area = math.pi*r*r
# print("Area of circle is :", area )

# # 7a
# print("Perimeter of Square\n")
# s = int(input("Enter the lenth of side: "))
# print("perimeter of square is ", 4*s)

# # 7e
# print("Perimeter of triangle\n")
# a = eval(input("Enter the side of triangle: "))
# b = eval(input("Enter the side of triangle: "))
# c = eval(input("Enter the side of triangle: "))
# print("perimeter of triangle is : ", a+b+c)

# # 7c
# import math
# print("Perimeter of circle")
# r = int(input("Enter the radius: "))
# perimeter = 2*math.pi*r
# print("perimeter of circle is :", perimeter )

# # 7b
# print("perimeter of rectangle")
# a = eval(input("enter side 1 of rectangle: "))
# b = eval(input("enter side 2 of rectangle: "))
# print("Perimeter of rectangle is :", 2*a*b)

# # 7d
# print("perimeter of tripazium")
# a = eval(input("enter side 1 of tripazium: "))
# b = eval(input("enter side 2 of tripazium: "))
# c = eval(input("enter side 3 of tripazium: "))
# d = eval(input("enter side 4 of tripazium: "))
# print("Perimeter of tripazium is :", a+b+c+d)

# 2 scientific
import math
def si(a):
    return math.sin(a)
def cos(a):
    return math.cos(a)
def tan(a):
    return math.tan(a)
def cosec(a):
    return (1/math.sin(a))
def sec(a):
    return (1/math.cos(a))
def cot(a):
    return (1/math.tan(a))
def Log(a):
    return math.log(a)
def radian(a):
    return math.radians(a)
def pi():
    return math.pi
if(__name__ == "__main__"):
    a = eval(input("Enter the value:"))
    print("""Enter the value corrosponding to the function
            sin = 1, cos = 2, tan = 3, cosec = 4, sec = 5
            cot = 6, log = 7, radian = 8, pi = 9""")
    fun = eval(input())
    if fun == 1:
        print(si(a))
    elif fun == 2:
        print(cos(a))
    elif fun == 3:
        print(tan(a))
    elif fun == 4:
        print(cosec(a))
    elif fun == 5:
        print(sec(a))
    elif fun == 6:
        print(cot(a))
    elif fun == 7:
        print(Log(a))
    elif fun == 8:
        print(radian(a))
    elif fun == 9:
        print(pi())
    else:
        print("Wrong input try again\n")
     
