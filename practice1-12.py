# 1.L1-[1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006] 
# From the above list, find the leap years and count the number of leap years in the list.

l1=["1234567890", "9876543210", "1234567890", "5555555555", "9876543210", "9999999999"]
print("our list is:",l1)
def duplicate():
    l2=[]
    for y1 in l1:
        if(y1 not in l2):
            l2.append(y1)
    print("our  new list is ",l2)

if (__name__=="__main__"):
    duplicate()

# 2.write a  code for showing all the arguement in various functions
# arguements in python
# positional arguements

def testcase(A,B,C):
    print("the value of A is",A)
    print()
    print("the value of B is",B)
    print()       
    print("the value of C is",C)
    print()
if(__name__=="__main__"):
    testcase(1000,2000,3000)

#default arguement

def testcase(A,B,C=100):
    print("the value of A is",A)
    print()
    print("the value of B is",B)
    print()       
    print("the value of C is",C)
    print()
if(__name__=="__main__"):
    testcase(1000,2000)

#keyword arguement
def test_case(eid,ename,esal,design):
    print("====product details====")
    print("eid is:",eid)
    print("ename is:",ename)
    print("esal is :",esal)
    print("design is:",design)
print()
if(__name__=="__main__"):
    test_case(eid=1001,ename="kishu",esal=40000,design="software developer")


#variable length argument
def testcase(*ihub):
    s1=0
    for x1 in ihub:
        s1=s1+x1
        print("sum is",s1)
    print(ihub)
if(__name__=="__main__"):
    testcase(10,20,30,40,50)
    print()
    testcase(10)
    print()
    testcase(10,20) 
    print()
    testcase(10,20,30)
    print()
    testcase(10,20,30,40)
    print()
    testcase(10,20,30,40,50)
    print()


#keyword variable length argument

def testcase(**a):
    for x1,y1 in a.items():
        print(x1,"===",y1)
if(__name__=="__main__"):
    testcase(eid=1001,ename="divya",esal="35000")
    print()
    testcase(eid=1002,ename="kishu",esal="40000")

# 3.write a code for simple calculator for +,-,,/,//* for two numbers ing function
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y
    
if __name__ == "__main__":
    num1 = eval(input("Enter the first number: "))
    num2 = eval(input("Enter the second number: "))
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter choice (1/2/3/4): ")
    
    if choice == '1':
        result = add(num1, num2)
        operator = '+'
    elif choice == '2':
        result = subtract(num1, num2)
        operator = '-'
    elif choice == '3':
        result = multiply(num1, num2)
        operator = '*'
    elif choice == '4':
        result = divide(num1, num2)
        operator = '/'
    else:
        print(" Please enter a valid operation (1/2/3/4).")

    print(f"\n{num1} {operator} {num2} = {result}")



# 4. str1="Success needs hardwork and patience" 
# Expected output="patience and hardwork needs Success"

str1 = "Success needs hardwork and patience"
b = str1.split()
a = " ".join(b[::-1])
print(a)

# 5.Write a logical and meaningful code for removing the duplicates mobile number.

l1=["1234567890", "9876543210", "1234567890", "5555555555", "9876543210", "9999999999"]
print("our list is:",l1)
def duplicate():
    l2=[]
    for y1 in l1:
        if(y1 not in l2):
            l2.append(y1)
    print("our  new list is ",l2)

if (__name__=="__main__"):
    duplicate()

# 6.print the following details using while loop in table format
# order_id=[]
# Customer_name=[] 
# Product=[]
# delivery_date=[]

# n=int(input("Enter number of row:"))
# for i in range(n):
#     A1=int(input("Ente the order id:"))
#     order_id.append(A1)
#     A2=input('Enter the Customer name:')
#     Customer_name.append(A2)
#     A3=input("Enter the Product:")
#     Product.append(A3)
#     A4=input('Enter the delivery date:')
#     delivery_date.append(A4)
# print()
# print("------------------------------------")
# print("order id", "Customer name","Product","delivery date",)
# print('-----------------------------------------')
# for x1,x2,x3,x4 in zip(order_id,Customer_name,Product,delivery_date):
#     print(x1,"  ",x2,"  ",x3,"  ",x4,)
# print("---------------------------------------------")
# print()


# order_id = []
# Customer_name = []
# Product = []
# delivery_date = []


l1 = []
x = 0
while x < len(l1):
    print(l1[x], end=", ")
    x += 1
print()
print("====================================================")
print("order id", "Customer name","Product","delivery date",)
print("====================================================")
l2 = [1111, "mahesh", "mobile", "2/12/2023"]
z = 0
while z < len(l2):
    print(l2[z], end="     ")
    z += 1
print()
l3 = [1112, "rajesh", "tv", "5/12/2023"]
x = 0
while x < len(l3):
    print(l3[x], end="     ")
    x += 1
print()
l4 = [1113, "dinesh", "laptop", "7/12/2023"]
h = 0
while h < len(l4):
    print(l4[h], end="     ")
    h += 1
print()
l5 = [1114, "suresh", "earbuds", "12/12/2023"]
a = 0
while a < len(l5):
    print(l5[a], end="     ")
    a += 1
print()
print("====================================================")

order_id = []
Customer_name = []
Product = []
delivery_date = []