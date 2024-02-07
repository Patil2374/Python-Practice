# #1
# class Animal:
#     def speak(self):
#         print('Animal Speaks')
# class Dog(Animal):
#     def overrides(self):
#         print('Dog barks')
# i = Animal()
# i.speak()
# a=Dog()
# a.overrides()

# #2
# class component:
#     def render(self):
#         print('Rendering component')
# class button(component):
#     def click(self):
#         print('Button clicked')
# class checkbox(button):
#     def check(self):
#         print('Checkbox checked')

# i=checkbox()
# i.render()
# i.click()
# i.check()

#3
class Employee:
    def details(self,name,salary):
        self.name=input("Enter the name  ")
        self.salary = float(input("Enter the salary  "))
        print()
        print('Name is  ',self.name)
        print("Salary is ",self.salary)
class manager(Employee):
    def attributes(self):
        print("==========Manager details==============\n")
class developer(Employee):
    def dev(self):
        print('==========Developer details=============\n')
i=manager()
i.attributes()
i.details(name=None,salary=None)
print()
a=developer()
a.dev()
a.details(name=None,salary=None)
print()

# #4
# class loggable:
#     def log(self):
#         print("Hello, You have loged in succesfully\n")
# class database:
#     def insert(self):
#         print('Inserted data\n')
#     def update(self):
#         print('updated data\n')
#     def delete(self):
#         print('deleted data\n')
# class loggedDatabase(loggable,database):
#     def log_database_operations(self):
#         print('Currently in log database operations\n')
# b=loggedDatabase()
# b.log()
# b.log_database_operations()
# b.insert()
# b.update()
# b.delete()