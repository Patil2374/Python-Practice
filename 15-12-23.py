# #1
# class emp_details:
#     Eid= 1001
#     Ename= "Anuj"
#     Esal= 25000
#     Company= "Cognizant"
#     def __init__(self):
#         pass
#     def m1():
#         print(emp_details.Esal)
#     @classmethod
#     def m2(cls):
#         pass
#     @staticmethod
#     def m3():
#         pass
# i = emp_details
# i.m1()
# print(emp_details.Eid)
# print(emp_details.Ename)
# print(emp_details.Esal)
# print(emp_details.Company)
# del emp_details.Eid ,emp_details.Company
# print(emp_details.__dict__) 


# # Q5
class gpay_rewards:  
    def __init__(self):
        username = input("Enter username: ")
        balance = 78000
        print(f"Dear {username}, Welcome to Google Play Rewards, Your Available balance is Rs {balance}")
        coupon_number = input("Enter Coupon Number ")
        if (coupon_number=='1122'):
            print("Congratulations! You have won Rs300/-")
        if (coupon_number=='1133'):
            print("Congratulations! You have won Rs289/-")
        if (coupon_number=='1111'):
            print("Congratulations! You have won Rs111/-")
        if (coupon_number=='1122'):
            balance+=300
            print(f"Your Available balance is {balance}")   
        if (coupon_number=='1133'):
            balance+=289
            print(f"Your Available balance is {balance}")    
        if (coupon_number=='1111'):
            balance+=111
            print(f" Your Available balance is {balance}")   
i=gpay_rewards()

