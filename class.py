#Demo: Classes in Python
#'self': it is the first argument passed to any function

class Person:
	def __init__ (self, name, age):
		self.name=name;
		self.age=age;
		
		
	def __init__ (self, name, age,person):
		self.name=name;
		self.age=age;
		self.person=person;
		
#Two objects are created. Init constructor is automatically called.
p1 = Person("Suppandi", 15)
p2 = Person("Ramu", 12)
p3 = Person("Bob",14, p2)

print("\nPerson #1, {}, is {} years old".format(p1.name, p1.age))
print("\nPerson #2, {}, is {} years old".format(p2.name, p2.age))

#Attributes of the object can be modified publicly
p2.age=10
print ("\nModified age of person #1 is", p2.age)

 #Printing after deleting age attribute for p1
del p1.age
 
print("\nName of person #1 is ", p1.name)
#print("Age of person #1 is", p1.age)   #...Attribute Error- p1.age does not exist
 
del p1
