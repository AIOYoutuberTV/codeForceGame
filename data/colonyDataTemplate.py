#from colonyData import ore,funds

class modifier():
	def __init__(self,magnitude):
		self.magnitude=magnitude
	   # self.system=system
	def applyModifier(self):
		return(self.magnitude)

class expert(): #unemployed
	def __init__(self,name,job,morale):
		self.name=name
		self.job=job
		self.morale=morale

class advisor(expert): #employed
	def __init__(self, name="NONE", job="NONE", morale="NONE", position="NONE", modifier:modifier=modifier(1)):
		super().__init__(name, job, morale)
		self.position=position
		self.modifier=modifier
	def applyBuff(self, factor):
		pass

class resource(): #N/A, ore, food, ec, data, morale,funds
	def __init__(self,name,count):
		self.count=count
		self.name=name
	def getValue(self):
		return self.count
	def setValue(self, amount):
		self.count=amount
	def getType(self):
		return self.name
	def get(self, amount):
		self.count += amount
	def spend(self, amount):
		self.count -= amount

class fund(resource):
	def __init__(self, name, count):
		super().__init__(name, count)

"""
class system(): #lifesupport, oreMining, culinary, electricityGen, research, morale
	def __init__(self,name,production:resource):
		self.name=name
		self.production=production
"""

class structure():
	def __init__(self,uuid,production:dict,consumption:dict,cost:int,count:int):
		self.uuid=uuid #TODO: implement a UUID generator (line 3)
		self.production=production
		self.consumption=consumption
		self.cost=cost
		self.count=count
	def useStructure(self):
		return self.production
#    def build(self, useOre, amount=1): #TODO: The building system broke.
#        if useOre == True:
#            ore.spend((self.cost[ore])*amount)
#        else:
#            funds.spend((self.cost[funds])*amount)
#        self.count += amount
	def getAmount(self):
		return self.count

class habitatStructure(structure):
	def __init__(self, uuid, habitatSize:int, consumption:dict, cost:int, count:int, production:dict={}):
		super().__init__(uuid,production,consumption,cost,count)
		self.habitatSize = habitatSize
	def getHabitatCapacity(self):
		return self.habitatSize * self.count
		
