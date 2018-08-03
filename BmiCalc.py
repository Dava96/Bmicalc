class Person(object):
	name = None
	height_mtr = None
	weight_kg = None
	
	def __init__(self, name, height_mtr, weight_kg):
		self.name = name
		self.weight_kg = weight_kg
		self.height_mtr = height_mtr
		
	def getWeight(self):
		return self.weight_kg
		
	def getHeight(self):
		return self.height_mtr
		
	def getName(self):
		return self.name
		
	def bmiForumula(self):
		bmi = self.weight_kg / (self.height_mtr ** 2)
		if bmi < 25:
			print(f"{self.name}'s bmi is {bmi}")
			print("This means you are not overweight")
		else:
			print(f"{self.name}'s bmi is {bmi}")
			print("This means you are overweight")
		
		
name = input("Enter your name here: ")
weight_kg = int(input("Enter your weight in kilograms here: "))
height_mtr = int(input("Enter your height in meters here: "))

Person1 = Person(name, height_mtr, weight_kg)

print(Person1.bmiForumula())
