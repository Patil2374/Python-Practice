# n = int(input("enter the number: "))
# if n%2==0:
#     print(n,'is a even number')
# else:
#     print(n,'is a odd number')


# even_odd = [x for x in range(101) if x%2==0]
# print(even_odd)

# def multiplication(a,b):
#     return a*b
# a = multiplication(5,6)
# print(a)


# n = int(input("Enter the number "))
# for i in range(2,n//2):
#     if n%i==0:
#         print(n,"is not a prime number")
#         break
# else:
#     print(n,'is a prime number')

# def factorial(n):
#         if n == 0 or n == 1:
#             return 1
#         else:
#             result = 1
#             for i in range(2, n + 1):
#                 result *= i
#             return result
# x = int(input("Enter the number: "))
# z= factorial(x)
# print(z)

# def is_armstrong_number(number):
#     n_str = str(number)    
#     power = len(n_str)   
#     armstrong_sum = sum(int(digit) ** power for digit in n_str)
#     return armstrong_sum == number

# number= int(input("Enter a number to check Armstrong : "))
# if is_armstrong_number(number):
#     print(f"{number} is an Armstrong number.")
# else:
#     print(f"{number} is not an Armstrong number.")

# class practice:
#     def m(self,*a):
#         z = 0
#         for i in a:
#             z = z+i
#         print("sum of any number of argumnet",z)
# p=practice()
# p.m(10)
# p.m(10,20)
# p.m(10,20,30)

# class practice:
#     def m(self,*a):
#         z = ''
#         for i in a:
#             z += str(i)
#         print("sum of any argumnet",z)
# p=practice()
# p.m('A')
# p.m("A","N")
# p.m("A","N","U")
# p.m("Anuj"," ","Patil")
