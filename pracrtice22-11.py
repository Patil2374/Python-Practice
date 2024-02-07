# What is function?
# =================
# A function can be represent as a peice of code or block of unit.The main objective
# of a function is provide the code resuability which means one write and call any number 
# of times.

# Types of Functions are:-
#    1. predefined
#    2. Userdefined

# Predefined Functions
# print(),id(),type(),eval()

# User defined are in below code

# mutliples of a number

def multiples(n):
    n= int(input("Entert the number:"))
    for i in range(1,11):
        print(n,"X",i,"=",n*i)
multiples(n=None)

# arguments in function
# Positional 
# Default
# Keyword
# Variable Length
# Keywords variable length

# # Positional 
# def marks(c,a,b):
#     print("English marks are: ",a)
#     print("Science marks are: ",b)
#     print("Maths marks are: ",c)

# if(__name__ == '__main__'):
#     marks(80,76,90)

# # Default

# def marks(a,b,c,d=0):
#     print("English marks are: ",a)
#     print("Science marks are: ",b)
#     print("Maths marks are: ",c)
#     print("Telgu marks are: ",d)


# if(__name__ == '__main__'):
#     marks(80,76,90)


# # Keyword

# def marks(a,b,c,d=0):
#     print("English marks are: ",a)
#     print("Science marks are: ",b)
#     print("Maths marks are: ",c)


# if(__name__ == '__main__'):
#     marks(a=80,b=76,c=90)

# # Variable Length

# def marks(*score):
#     for i in score:
#         print("Marks are: ",i)

# if(__name__ == '__main__'):
#     marks(80,76,90)


# # Keywords variable length

# def marks(**s):
#     for i,j in s.items():
#         print(i,"---",j,"\n")

# if(__name__ == '__main__'):
#     marks(Eid=101,Ename="Kajal Agrawal",Occupation="Actor",income=2 )

# # Finding the prime number using functions

# def prime_numbers(num):
#     if num > 1:
#         for i in range(2, int(num)):
#             if (num % i) == 0:
#                 print(num, "is not a prime number\n")
#                 break
#         else:
#             print(num, "is a prime number\n")

# if(__name__ == '__main__'):
#     num = eval(input("Enter the number: "))
#     prime_numbers(num)

# # check if a year is leap Year or not

# def check_leap_year(s):
#     for i in s:
#         if(i % 100 == 0 and i % 400 == 0):
#             print(i,"is a leap year\n")
#         elif(i % 4==0):
#             print(i,"is a leap year\n")
#         else:
#             print(i,"is not a leap year\n")

# if(__name__ == "__main__"):
#     l1 = [2000,2001,2002,2003,2004,2005,2006,2007,2008]
#     check_leap_year(l1)

# #factorial of a number 

# def fact(n):
#     return 1 if (n==1) else n*fact(n-1)

# if(__name__ == "__main__"):
#     print(fact(5),"\n")
