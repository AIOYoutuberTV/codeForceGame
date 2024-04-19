from random import randint

uuidCounter=0

class colonist():
    def __init__(self,name,job,morale):
        self.name=name
        self.job=job
        self.morale=morale

class advisor(colonist): #employed
    def __init__(self, name, job, morale, position, modifier):
        super().__init__(name, job, morale)
        self.position=position
        self.modifier=modifier
    def applyBuff(self, factor):
        pass
 
class resource(): #N/A, ore, food, ec, data, morale
    def __init__(self,name,value):
        self.value=value
        self.name=name
    def getValue(self):
        return self.value
    def setValue(self, amount):
        self.value=amount
    def getType(self):
        return self.name
    def addValue(self, amount):
        self.value += amount

"""
class system(): #lifesupport, oreMining, culinary, electricityGen, research, morale
    def __init__(self,name,production:resource):
        self.name=name
        self.production=production
"""

class structure():
    def __init__(self,uuid,production:resource,consumption:resource):
        self.uuid=uuid #TODO: implement a UUID generator (line 3)
        self.production=production
        self.consumption=consumption
    def useStructure(self):
        pass #TODO: Come back to this later.

class modifier():
    def __init__(self,magnitude):
        self.magnitude=magnitude
       # self.system=system
    def applyModifier(self):
        return(self.magnitude)

ore = resource("Ore",0)
food = resource("Food",0)
ec = resource("Electric Charge",0)
science = resource("Research Points",0)
lifeSupport = resource("Life Support Intregity",0)

lifeSupportSys = system("Life Support",) #TODO: Add further systems after making psudocode.
