"""Name
age
year
class teacher name
    Year born
        address
            Emergency contact number/Email"""

class student_profile():
    def __init__(self,name,age,year,class_teacher_name,students, year_born,address,emergency_contact):
        self.name = name
        self.age = age
        self.year = year
        self.class_teacher_name = class_teacher_name
        self.students = students
        self.year_born = year_born
        self.address = address
        self.emergency_contact = emergency_contact
    def display(self):
        print(self.name,self.age,self.year,self.class_teacher_name,self.students,self.year_born,self.address,self.emergency_contact)
        

#object of the class
s1 = student_profile("Rahim","12","8","Ms Baldassare","30","2012","123 Ohio Street","The C.A.T")
s2 = student_profile("Bobby","14","9","Mr LaLaLaLa","27","2009","456 Meow Road","The D.O.G")
s3 = student_profile("Jay","16","11","Ms GrrrrBA","24","2007","789 Coding Street","The B.U.N.N.Y")

run = True

s1.display()
s2.display()
s3.display()
