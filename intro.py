
# 🧩 Task 1: Student System
# 👉 Question:Create a class Student with:Class variable: school_name = "XYZ School"
# A method set_details(),→ inside method, assign:name = "Vamsi",marks = 85,A method display()
#  → print:Name,Marks,School name
# 👉 Outside the class:Create object,Call set_details(),Call display()

class student:
    school_name = "KSR school"
    def set_details(self):
        self.name = "vamsi"
        self.marks = 85 
    def display(self):
        print(self.name,self.marks,self.school_name)
S = student()
S.set_details()
S.display()


# 🧩 Task 2: Employee System
# 👉 Question:
# Create a class Employee with:Class variable: company = "Infosys",A method set_data()
# assign:,name = "Ravi",salary = 20000,A method increase_salary(), add 5000 to salary
# A method display(),print all details
# 👉 Outside the class:Create object,Call all methods

class Employee:
    company = "infosys"
    def set_data(self):
        self.name = "ravi"
        self.salary = 20000
    def increase_salary(self):
        self.salary= self.salary +5000
    def display(self):
        print(self.name)
        print(self.company)
        print(self.salary)
C = Employee()
C.set_data()
C.increase_salary()
C.display()

# 🧩 Task 3: Mobile System
# 👉 Question:Create a class Mobile with:Class variable: brand = "Apple",A method set_details()
# assign:model = "iPhone 14",price = 80000,A method discount(), reduce price by 10%
# A method show_details(), print all details,Outside the class: Create object,Call methods

class Mobile:
    brand = "Apple"
    def set_details(self):
        self.model = "iPhone 14"
        self.price = 80000
    def discount(self):
        self.price *= 0.9  
        # (self.price * 10/100)

    def show_details(self):
        print(self.model,self.brand,self.price)

E = Mobile()
E.set_details()
E.discount()
E.show_details()


    





