# n =
# for i in range(4):
#     for j in range(4):
#         print(n,end =" ")
#     print()
#     n +=1

# n= 2
# for i in range(4):
#     for j in range(4):
#             print(n,end=" ")
#     n+=2
#     print()

# l1 = "listen" 
# l2 = "silent"
# for i in range(len(l2)):
#     if l2[i] not in l1:
#         print("Not an anagram")
#         break
# else:
#     print("It is Anagram")

# n=2
# for i in range(1, 5):
#     for j in range(4):
#             if n==2:
#                   print(n,end=" ")
            
#             else:
#                 print(n*n,end=" ")
#     n+=1
#     print()

# l = ['A','B','C']
# for i in range(3):
#     print(l)
    
# l1 = [1,2,3,4,5,6]
# l2 = [7,8,9,10,11,12]
# l1 = l1+l2
# print(l1)

1
wh =int(input("Enter worked hours :"))
if wh < 8:
    b=350*wh
    print(b)
else:
    overtime = wh - 8
    a = 8 *350
    d = overtime *525
    c = a + d
print(c)

# 4
class employee:
    def init(self):
        eid=101
        ename="vasu"
        esal=29000
        company="tcs"
        print(eid,ename,esal,company)
i1=employee()

# 2
l1 = [1,2,3,4,5,6]
l2 = [7,8,9,10,11,12]
l3 = [*l1,*l2]
print(l3)

class FactorialCalculator:
    def calculate_factorial(self, n):
        if n < 0:
            return "Factorial is not defined for negative numbers."
        elif n == 0 or n == 1:
            return 1
        else:
            result = 1
            for i in range(2, n + 1):
                result *= i
            return result

if __name__ == "__main__":
    calculator = FactorialCalculator()
    number = int(input("ENTER THE NUMBER  "))
    result = calculator.calculate_factorial(number)
    print(f"The factorial of {number} is: {result}")
