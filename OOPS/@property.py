class Student:
    def __init__(self,name,school):
        self.name=name
        self.school=school
        self.marks=[]

    def average(self):
        return sum(self.marks)/len(self.marks)

    @property
    def weekly_salary(self):
        return self.salary*5

class WorkingStudent(Student):
    def __init__(self,name,school,salary):
        super().__init__(name,school)
        self.salary=salary

rolf=WorkingStudent('r','aa',15)
print(rolf.weekly_salary)

dict={
    range(0,23):0,
    range(23,43):23,
    range(43,63):43,
    range(63,83):63,
    range(83,1):1
}
print(dict[22])