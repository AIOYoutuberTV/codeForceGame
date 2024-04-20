from random import randint
from .. import *
import uuid
from data.colonyData import *

version = "indev-0.0.1"

uuidCounter=0


class expert(): #unemployed
    def __init__(self,name,job,morale):
        self.name=name
        self.job=job
        self.morale=morale

class advisor(expert): #employed
    def __init__(self, name, job, morale, position, modifier):
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
    def __init__(self,uuid,production:dict,consumption:dict,cost:dict,count:int):
        self.uuid=uuid #TODO: implement a UUID generator (line 3)
        self.production=production
        self.consumption=consumption
        self.cost=cost
        self.count=count
    def useStructure(self):
        pass #TODO: Come back to this later.
    def build(self, amount, useOre):
        if useOre == True:
            ore.spend(self.cost[ore])
        self.count += amount


class modifier():
    def __init__(self,magnitude):
        self.magnitude=magnitude
       # self.system=system
    def applyModifier(self):
        return(self.magnitude)

class colony():
    def __init__(self,name:str,colonists:int,
                 ore:resource,food:resource,energy:resource,science:resource,lifeSupport:resource,funds:resource,
                 solarPanel:structure):
       self.uuid=uuid.uuid1()
       self.name = name
       self.colonists = colonists
       self.ore = ore
       self.food = food
       self.energy = energy
       self.science = science
       self.lifeSupport = lifeSupport
       self.funds = funds
       self.solarPanel = solarPanel