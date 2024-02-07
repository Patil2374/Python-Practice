# Q2
class product_details:
    def __init__(self):
        self.pid=101
        self.pname="dell"
        self.price=40000
        self.model="inspirion"
    def m1(self):
        print("product id is:",self.pid)
        print("product name is :",self.pname)
        print(" product price is:",self.price)
        print("model is:",self.model)   
i1=product_details()
print()
print(i1.__dict__)      
print()

# Q3
class person:
    def __init__(self):
        self.age = 35
        self.name = "Anuj"
    def person_info(self):
        print("Person's name is ",self.name)
        print("Person's age is ",self.age)
a = person()
a.person_info()

# Q4
class Rectangle:
    def __init__(self):
        self.length = 35
        self.width = 10
    def calculate_area(self):
        print("Area of rectangle is ",self.length * self.width)
    def calculate_perimeter(self):
        print("Perimeter of rectangle is ",(self.length * self.width)*2)
a = Rectangle()    
a.calculate_area()
a.calculate_perimeter()

# Q1
class students ():
    def __init__(self):
      self.st_name='Anuj'
      self.st_id='72031725J'
      self.st_rank="01"
    def Sinhgad(self):
       self.st_name="Shubham"
       self.st_id='121'
       self.st_rank='02'
       self.st_report_card='75%'
       del self.st_report_card
    @classmethod   
    def Sinhgad_1(cls):
       pass
    @staticmethod
    def Sinhgad_2():
       pass
i1=students()
print(i1.__dict__)
print()
i1.Sinhgad()
i1.st_name1='rahul'
i1.st_id_2='122'
i1.st_rank_3="01"
i1.st_review4="All time record"
print()
print(i1.__dict__)
print()

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    def calculate_average(self):
        total = sum(self.grades)
        average = total / len(self.grades)
        return average
student1 = Student("Anuj", [90, 85, 92, 88, 95])
average_grade = student1.calculate_average()
print(f"{student1.name}'s average grade is: {average_grade}")
