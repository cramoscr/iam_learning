# 14_classes_lab.py
# Based on Python Crash Course book (page 159)
# Updated: cramos 08/jun/2022

# Notes:
#   In this lab we will follow:
#        pascalCase format for parameter
#        CamelCase format for classes

#   I really liked how Pyhton handles inheritance... 
#      (a lot easier than Java or JS)

# OOP: abstraction, encapsulation, inheritance, polymorphism
#      Python doesn't provides encapsulation natively :(

# Example 1
print ("\n 1___ Creating a basic Class object ___\n")

class Vehicle:
	""" First attempt to define a Vehicle as a class """
	def __init__(self, pBrand, pType, pColor, pId):
		"""Initialize Vehicle attributes"""
		self.brand = pBrand
		self.type = pType
		self.color = pColor
		self.id = pId
		self.engine_status = 'off'
		self.light_status = 'off'
		print(f"Vehicle initialization finished...")

	def start_engine(self):
		""" Simulates the Vehicle engine start """
		print(f"{self.brand} {self.id} engine is now started...")
		self.engine_status = 'on'

	def turn_lights_on(self):
		""" Simulates the Vehicle lights turned on """
		print(f"{self.brand} {self.id} ligths are now ON...")

my_vehicle = Vehicle('Toyota','Sedan','Blue','BHT-144')

print(f"my_vehicle class: {my_vehicle}")

my_vehicle.turn_lights_on()
my_vehicle.start_engine()

# Algo medio feito... 
#    Puedo tener acceso a los atributos "desde afuera"
print(f"Vehicle color: {my_vehicle.color}")
my_vehicle.color = 'red'
print(f"Car color: {my_vehicle.color}")


# Example 2
print ("\n 2___ Inheritance ___\n")

class Car(Vehicle):
	""" This class extends the Vehicle by adding specific Car features """
	def __init__(self, pBrand, pType, pColor, pId, pDoorsQty, pTraction ):
		""" Initializes parent Class first, then specific Car features"""
		super().__init__(pBrand, pType, pColor, pId)
		self.doorsqty = pDoorsQty
		self.traction = pTraction
		print(f"Car initialization finished...")

	#def start_engine(self):
	#	""" Simulates the Car engine start """
	#	super().start_engine()

	#def turn_lights_on(self):
	#	""" Simulates the Car lights turned on """
	#	super().turn_lights_on()

my_car = Car('Toyota','Sedan','Dark Red','BHT-144', 5, '4x4')

print(f"my_car class: {my_car}")

my_car.turn_lights_on()
my_car.start_engine()

print(f"Car color: {my_car.color}")
print(f"Car doors: {my_car.doorsqty}")
print(f"Car traction: {my_car.traction}")


# Example 3
print ("\n 3___ Inheritance + Methods overriding ___\n")

class Truck(Vehicle):
	""" This class extends the Vehicle by adding specific Truck features """
	def __init__(self, pBrand, pType, pColor, pId, pWheelsQty, pWeightLoad ):
		""" Initializes parent Class first, then specific Truck features"""
		super().__init__(pBrand, pType, pColor, pId)
		self.wheels = pWheelsQty
		self.weightcap = pWeightLoad
		print(f"Truck initialization finished...")

	#def start_engine(self):
	#	""" Simulates the Car engine start """
	#	super().start_engine()

	def turn_lights_on(self):
		""" Overrides the parent method - lights turned on """
		self.light_status = 'on'
		print(f"Se prendió el portal de belén")

my_truck = Truck('Freightliner','Narizon','Gold','TOTO-x1', 12, '10 toneladas')

my_truck.turn_lights_on()
my_truck.start_engine()

print(f"my_truck class: {my_truck}")
print(f"Lights status: {my_truck.light_status}")
print(f"Wheels qty: {my_truck.wheels}")

