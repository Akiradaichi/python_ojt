# 1
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def myfunc(self):
        print("a first name of employee is " + self.fname)
p1 = Person("John", "Nathan")
p1.myfunc()
class Employee(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
emp = Employee("Authur", "King")
emp.myfunc()

# 2
l = list(range(1, 11))
iter_l = l.__iter__()
print(iter_l.__next__())
print(iter_l.__next__())
print(iter_l.__next__())
print(iter_l.__next__())
print(iter_l.__next__())
print(iter_l.__next__())
print(iter_l.__next__())
print(iter_l.__next__())
print(iter_l.__next__())
print(iter_l.__next__())