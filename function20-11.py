# L1 = ("Pid","Pname","Price","Company","M_date","Exp_date")
# L2 = ()
# def Test_Case1():
#     Pid=int(input('Enter the Pid:'))
#     Pname=input('Ener the Pname:')
#     Price=float(input('Enter the Price:'))
#     Company=input('Enter the Company:')
#     M_date=input('Enter rhe M_date:')
#     Exp_date=input('Enter the Exp_date:')
#     print()
#     L2.insert(Pid)
#     L2.insert(Pname)
#     L2.insert(Price)
#     L2.insert(Company)
#     L2.insert(M_date)
#     L2.insert(Exp_date)
#     return L2

# if(__name__=="__main__"):
#     L2 = Test_Case1()
#     L3 = zip(L1,L2)

# for i in range(len(L2)):
#     print(L3[i].values)
# print()

# def read_employee_records(records, num_records):
#     for i in range(num_records):
#         name = input(f"Enter name of employee {i + 1}: ")
#         age = int(input(f"Enter age of employee {i + 1}: "))
#         salary = float(input(f"Enter salary of employee {i + 1}: "))

#         # Create a dictionary for each employee
#         employee_data = {
#             "Name": name,
#             "Age": age,
#             "Salary": salary
#         }

#         # Append the employee data to the records list
#         records.append(employee_data)

# def display_employee_records(records, num_records_to_display):
#     print("\nEmployee Records:")
#     for i in range(min(num_records_to_display, len(records))):
#         employee = records[i]
#         print(f"Employee {i + 1}: {employee}")

# # Create an empty list to store employee records
# employee_records = []

# # Call the function to read employee records
# read_employee_records(employee_records, 1)

# # Call the function to display the first 5 employee records
# display_employee_records(employee_records, 1)


# def read_employee_records(records, num_records):
#     for i in range(num_records):
#         name = input(f"Enter name of employee {i + 1}: ")
#         age = int(input(f"Enter age of employee {i + 1}: "))
#         salary = float(input(f"Enter salary of employee {i + 1}: "))

#         # Create a dictionary for each employee
#         employee_data = {
#             "Name": name,
#             "Age": age,
#             "Salary": salary
#         }

#         # Append the employee data to the records list
#         records.append(employee_data)

# def display_employee_records(records):
#     print("\nEmployee Records:")
#     for i, employee in enumerate(records, start=1):
#         print(f"Employee {i}: {employee}")

# # Create an empty list to store employee records
# employee_records = []

# # Call the function to read and display employee records
# read_employee_records(employee_records, 1)
# display_employee_records(employee_records)

# num_records = int(input("Enter the no. of records you want:  "))
# employee_records = []
# def read(records,num_records):
#     for i in range(num_records):
#         name = input(f"Enter name of employee {i + 1}: ")
#         age = int(input(f"Enter age of employee {i + 1}: "))
#         salary = float(input(f"Enter salary of employee {i + 1}: "))

#     employee_data = {
#             "Name": name,
#             "Age": age,
#             "Salary": salary
#         }
#     records.append(employee_data)

# if(__name__ == '__main__'):
#     read(employee_records,num_records)
#     for i in employee_records:
#         print(f"Employee {i}: {i}")