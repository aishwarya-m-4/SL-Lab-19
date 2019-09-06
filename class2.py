class Person:
	def __init__ (self, name, age):
		self.name=name;
		self.age=age;
		
#Two objects are created. Init constructor is automatically called.
p1 = Person("Suppandi", 15)

print("Person #1, {}, is {} years old".format(p1.name, p1.age))
 #Prinitng after deleting age attribute for p1
del p1.age
 
print("Name of person #1 is ", p1.name)
#print("Age of person #1 is", p1.age)   #...Attribute Error- p1.age does not exist
 
del p1
