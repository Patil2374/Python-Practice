# # 6.print the following details using for loop and while loop in table format
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

# while loop 

# l1 = []
# x = 0
# while x < len(l1):
#     print(l1[x], end=", ")
#     x += 1
# print()
# print("====================================================")
# print("order id", "Customer name","Product","delivery date",)
# print("====================================================")
# l2 = [1111, "mahesh", "mobile ", "2/12/2023"]
# z = 0
# while z < len(l2):
#     print(l2[z], end="     ")
#     z += 1
# print()
# l3 = [1112, "rajesh", "tv     ", "5/12/2023"]
# x = 0
# while x < len(l3):
#     print(l3[x], end="     ")
#     x += 1
# print()
# l4 = [1113, "dinesh", "laptop ", "7/12/2023"]
# h = 0
# while h < len(l4):
#     print(l4[h], end="     ")
#     h += 1
# print()
# l5 = [1114, "suresh", "earbuds", "12/12/2023"]
# a = 0
# while a < len(l5):
#     print(l5[a], end="     ")
#     a += 1
# print()
# print("====================================================")

# order_id = []
# Customer_name = []
# Product = []
# delivery_date = []

# # 5 print the pattern
def triangle(n):
	k = n - 1
	for i in range(0, n):
		for j in range(0, k):
			print(end=" ")
		k = k - 1
		for j in range(0, i+1):
			print("* ", end="")
		print("\r")
n = 5
triangle(n)
