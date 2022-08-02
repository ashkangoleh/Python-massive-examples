# from statistics import mean


# my_student = {
#     "name": "Student",
#     "grade": [70, 88, 90, 99],
#     "average": None
#     }


# def average_grade(student):
#     return mean(student.get('grade'))


# class Student:
#     def __init__(self, new_name: str, new_grade: list[int]) -> None:
#         self.name = new_name
#         self.grades = new_grade
        
#     def average_grade_non_deco(self) -> int:
#         return mean(self.grades)
    
#     @property
#     def average_grade(self) -> int:
#         return mean(self.grades)


# student_n1 = Student(new_name="ashkan",new_grade=[91,99,88,93])
# print(student_n1.average_grade_non_deco()) # with no property decorator
# print(student_n1.average_grade) # with property decorator

# student_n2 = Student(new_name="ashkan",new_grade=[10,20,30,40])

# #there is an another way to use class and method
# print(Student.average_grade_non_deco(student_n2)) # not recommended



class Employee:
    def __init__(self, name, salary=30000):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

        
class Manager(Employee):
    def display(self):
        print("Manager ", self.name)

    def __init__(self, name, salary=50000, project=None):
        Employee.__init__(self, name, salary)
        self.project = project

    # Add a give_raise method
    def give_raise(self, amount, bonus=1.05):
        new_amount = amount * bonus
        Employee.give_raise(self, new_amount)
    
    
mngr = Manager("Ashta Dunbar", 78500)
mngr.give_raise(1000)
print(mngr.salary)
mngr.give_raise(2000, bonus=1.03)
print(mngr.salary)