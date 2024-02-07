# Python program to write functions for different operations

# def sum(a,b):
#     return a+b

# def diff(a,b):
#     return a-b

# def mult(a,b):
#     return a*b

# def div(a,b):
#     return a/b

# if __name__ == '__main__':
#     a = 20
#     b = 10
#     print(sum(a,b))
#     print(diff(a,b))
#     print(mult(a,b))
#     print(div(a,b))


# Python program to determine whether the number is palindrome number or not

# def palindrome(a):
#     if(a[0:] == a[::-1]):
#         return "It is palindrome"
#     else:
#         return "Not palindrome"
    
# if __name__ == '__main__':
#     str = input("Enter data to check palindrome or not")
#     print(palindrome(str))

# Python program to determine whether the number is Armstrong number or not

# def power(x, y):
# 	if y == 0:
# 		return 1
# 	elif y % 2 == 0:
# 		return power(x, y // 2) * power(x, y // 2)		
# 	else:
# 		return x * power(x, y // 2) * power(x, y // 2)

# def isArmstrong(x):
	
# 	n = len(str(x))
# 	temp = x
# 	sum1 = 0
# 	while (temp != 0):
# 		r = temp % 10
# 		sum1 = sum1 + power(r, n)
# 		temp = temp // 10
# 	return (sum1 == x)

# x = int(input("Enter no to check armstrong or not"))
# print(isArmstrong(x))

#write a code for ap and fp for student details

# def student_details(name,marks,grade):
#     print("====formal parameters====")
#     print("name is",name)
#     print("marks is",marks)    
#     print("grade is",grade)
# if (__name__=="__main__"):
#     student_details("Anuj",97,"A+")