from abc import ABC,abstractmethod

class person(ABC):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @abstractmethod
    def role(self):
        pass    

class Student(person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id=student_id
        self.enrolled_courses=[]
    def get_role(self):
        return "Student"
    def get_enrolled_courses(self,course_name):
        self.enrolled_courses.append(course_name)

class course:
    def __init__(self,course_name,course_code):
        self.course_name=course_name
        self.course_code=course_code
        self.teacher=None
        self.enrolled_students=[]
    def set_teacher(self,teacher_name):
        self.teacher=teacher_name

    def add_student(self,student_name):
        if student_name not in self.students_name:
            self.student_name.append(student_name)

    def course_info(self):
        return{
            "course":self.course_name,
            "code":self.course_code,
            "Teacher":self.teacher.name if self.teacher else "not assigned",
            "students":[s.name for s in self.students]

        }
    
class Department:
    def __init__(self,department_name):
        self.department_name=department_name    
        self.course=[]
        self.teachers=[]
        self.students=[]
    def add_course(self,course):
        self.courses.append(course)

    def add_teacher(self,teacher):
        self.teachers.append(teacher) 

    def add_students(self,student):
        self.students.append(student) 

    def summary_info(self):
        return {
            "Department": self.department_name,
            "Courses": [c.course_name for c in self.courses],
            "Teachers": [t.name for t in self.teachers],
            "Students": [s.name for s in self.students]
        }
class Administration:
    def __init__(self):
        self.departments = []

    def add_department(self, dept):
        self.departments.append(dept)

    def department_info(self):
        return [dept.summary_info() for dept in self.departments]  


s1=Student("Alice")
s2=Student("Mona",21,"s103")
c1=course("python programming","CSE")
s1.enrolled_courses(c1)
s2.enrolled_courses(c1)
dept=Department("computer science")
dept.add_course(c1)
dept.add_students(s1)
dept.add_students(s2)
print(c1.course_info)
print(dept.summary_info())




        

       


     
