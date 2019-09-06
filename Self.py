class Person:
    def __init__(self,name,age): #This is the constructor of the class Person
        self.name=name
        self.age=age

p1=Person("Suppandi",14)
p2=Person("Ramu",12)

print("\nName of person #1 is",p1.name)
print("\nAge of person #1 is",p1.age)

print("\nName of person #2 is",p2.name)
print("\nAge of person #2 is",p2.age)

p2.age=10
print("\nAge of person #2 is",p2.age)

del p1.age
print("\nName of person #1 is",p1.age)



