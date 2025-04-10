class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def return_name(self):
        return self.name


andrew = 'andrew'
student = Student(andrew, 5)
print(student.name)
