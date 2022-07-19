from statistics import mean


my_student = {
    "name": "Student",
    "grade": [70, 88, 90, 99],
    "average": None
    }


def average_grade(student):
    return mean(student.get('grade'))


class Student:
    def __init__(self, new_name: str, new_grade: list[int]) -> None:
        self.name = new_name
        self.grades = new_grade
        
    def average_grade_non_deco(self) -> int:
        return mean(self.grades)
    
    @property
    def average_grade(self) -> int:
        return mean(self.grades)


student_n1 = Student(new_name="ashkan",new_grade=[91,99,88,93])
print(student_n1.average_grade_non_deco()) # with no property decorator
print(student_n1.average_grade) # with property decorator

student_n2 = Student(new_name="ashkan",new_grade=[10,20,30,40])

#there is an another way to use class and method
print(Student.average_grade_non_deco(student_n2)) # not recommended