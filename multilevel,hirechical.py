class School:
    def __init__ (self):
        self.school_name = "KSR HIGH SCHOOL"
        
    def show_school(self):
        print("School Name",self.school_name)
        
class Teacher(School):
    def __init__(self):
        self.teacher_name = "Durga prasad"
        self.subject = "physics"
        
        super().__init__()
        
    def show_teacher(self):
        print(self.teacher_name,self.subject)
class Student(Teacher):
    def __init__(self,student_name,grade):
        
        self.student_name = student_name
        self.grade = grade
        super().__init__()
        
    def show_student(self):
        print("Student:",self.student_name,"Grade:",self.grade)
    
S1= Student("yaswanth","A")
S2 = Student("narasimha","B")
S1.show_school()
S1.show_teacher()
S1.show_student()

S2.show_school()
S2.show_teacher()
S2.show_student()


class User:
    def __init__(self):
        self.name = "Durga Prasad"
        self.location = "Hyderabad"
       
    def login(self):
        print("USER:",self.name,"LOCATION:",self.location)
class Customer(User):
    def __init__(self):
        self.order_item = "Biryani"
        super().__init__()
    def place_order(self):
            print("ORDER ITEM:",self.order_item)
class DeliveryPartner(User): 
    def __init__(self):
        self.vehicle_type = "Two Wheeler"
        super().__init__()
    def deliver_order(self):
            print("VEHICLE:",self.vehicle_type)

c1=Customer()
c2=DeliveryPartner()

c1.login()
c1.place_order()

c2.login()
c2.deliver_order()