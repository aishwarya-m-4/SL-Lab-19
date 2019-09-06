class Student:
    def __init__(self):
        self.name=0
        self.age=0
    def display(self):
        print(self.name)
        print(self.age)
        print(self.marks)
    def accept(self):
        self.marks = input("Enter the subject marks, separated by blank spaces")
        self.marks=list((self.marks.split(' ')))
        name=input("Enter name")
        age=input("Enter age")

        self.name=name
        self.age=age

p1=Student()
p1.accept()
p1.display()