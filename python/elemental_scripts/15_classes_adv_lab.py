# 14_classes_adv_lab.py
# Based on Python Crash Course book (page 177)
# Updated: cramos 08/jun/2022

# Example 1
print ("\n 1___ Creating a Class using composition ___\n")

class Vehicle:
	""" General Vehicle class definition """
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

class Engine:
	""" Engine class definition for a vehicle """
	def __init__(self, pFuelType, pSize, pTransmission):
		"""Initialize Vehicle attributes"""
		self.fueltype = pFuelType
		self.size = pSize                # expressed in cubic centimeters
		self.transmission = pTransmission  # values: automatic / manual

class Truck(Vehicle):
	""" This class extends the Vehicle and uses Engine class """
	def __init__(self, pBrand, pType, pColor, pId, pWheelsQty, pWeightLoad, pEngineFT, pEngineSz, pEngineTx ):
		""" Initializes parent Class first, then specific Truck features"""
		super().__init__(pBrand, pType, pColor, pId)
		self.wheels = pWheelsQty
		self.weightcap = pWeightLoad
		self.engine = Engine(pEngineFT, pEngineSz, pEngineTx)
		print(f"Truck initialization finished...")

	def turn_lights_on(self):
		""" Overrides the parent method - lights turned on """
		self.light_status = 'on'
		print(f"Se prendió el portal de belén")

my_truck = Truck('Freightliner','Narizon','Gold','TOTO-x1', 12, '10 toneladas', 
	              'diesel', '3000cc', 'manual')

my_truck.turn_lights_on()
my_truck.start_engine()

print(f"my_truck class: {my_truck}")
print(f"Lights status: {my_truck.light_status}")
print(f"Wheels qty: {my_truck.wheels}")
print(f"\nEngine:")
print(f"\tFuel: {my_truck.engine.fueltype}")
print(f"\ttransmission: {my_truck.engine.transmission}")


# Example 2
print ("\n 2___ Collections ___\n")


# Example 3
print ("\n 3___ Importing classes ___\n")

