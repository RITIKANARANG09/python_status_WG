class Student:
    def __init__(self,name,school):
        self.name=name
        self.school=school
        self.marks=[]

    def average(self):
        return sum(self.marks)/len(self.marks)

    def weekly_salary(self):
        return self.salary*5

class WorkingStudent(Student):
    def __init__(self,name,school,salary):
        super().__init__(name,school)
        self.salary=salary

rolf=WorkingStudent('r','aa',15)
print(rolf.salary)
rolf.marks.append(2)
rolf.marks.append(4)
print(rolf.average())
print(rolf.weekly_salary())