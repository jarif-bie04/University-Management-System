class Person:
    total_count = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.total_count += 1
        
    def introduce(self):
        print(f"Hi, I am {self.name}, {self.age} years old.")
        
    def display_role(self):
        pass
    
    @classmethod
    def get_total_people(cls):
        return cls.total_count
    

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.course_list = []
        self.__gpa = None
        
    def enroll_course(self, course):
        self.course_list.append(course)
    
    def show_courses(self):
        print("Enrolled Courses:")
        for course in self.course_list:
            print(f"- {course}")
            
    def display_role(self):
        print("I am a student at the university.")   
        
    @property
    def gpa(self):
        return self.__gpa
    
    @gpa.setter
    def gpa(self, value):
        if (value >=0 and value <=4.0):
            self.__gpa = value
            print(f"GPA = {self.gpa}")
        else:
            print("ERROR in GPA!!!")
            
            
    @staticmethod
    def  is_valid_id(student_id):
        if len(student_id) > 2:
            if(student_id[0] == "S" and student_id[1] == "-"):
                return f"Valid Student ID"
            else:
                return f"Invalid Student ID"
        else:
            return f"Invalid Student ID"
        
        
class GraduateStudent(Student):
    def __init__(self, name, age, student_id,  thesis_title):
        super().__init__(name, age, student_id)
        self.thesis_title = thesis_title
        
    def show_details(self):
        print(f"Graduate Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")
        print(f"Thesis Title: {self.thesis_title}")
     

class Teacher(Person):
    def __init__(self, name, age, employee_id, subject):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.subject = subject
        
    def introduce(self):
        print(f"I am Professor {self.name}, teaching {self.subject}.")

    def display_role(self):
        print("I am a teacher at the university.")
        
        



# # Example usage

# per1 = Student("Jarif", 21, "2409001")
# per1.introduce()
# per1.enroll_course("Mathematics")
# per1.enroll_course("Physics")
# per1.enroll_course("Chemistry")
# per1.show_courses()
# per1.display_role()
# per1.gpa = 5
# # print(per1.gpa)

# print("----------------------------------------------------------------")

# per2 = Teacher("Dr. Rakib Hasan", 45, "T1001", "Computer Science")
# per2.introduce()
# per2.display_role()

# print("----------------------------------------------------------------")

# print(f"Total Objects have been created = {Person.get_total_people()}")

# print("----------------------------------------------------------------")
# print(Student.is_valid_id("A-12345"))
# print(Student.is_valid_id("S-12345"))

# print("----------------------------------------------------------------")
# per3 = GraduateStudent("Ibn Anik", 23, "S-1234567", "ABCD")
# per3.show_details()
# per3.gpa = 3

# print("----------------------------------------------------------------")

# print(f"Total Objects have been created = {Person.get_total_people()}")