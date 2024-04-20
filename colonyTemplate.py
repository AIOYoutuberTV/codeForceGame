import uuid
from colonyDataTemplate import *
from data.colonyData import *
import json

class colony():
    def __init__(self,name:str,colonists:int,activeAdvisor:advisor,
                 ore:resource=ore,food:resource=food,energy:resource=energy,science:resource=science,lifeSupport:resource=lifeSupport,funds:resource=funds,
                 habitat:habitatStructure=habitat,solarPanel:structure=solarPanel,mine:structure=mine,farm:structure=farm,atmosphereicUnit=atmosphericUnit):
       #colony attributes
       self.uuid=uuid.uuid1()
       self.name = name
       self.colonists = colonists
       self.populationLimit = self.habitat.getHabitatCapacity()
       self.activeAdvisor = activeAdvisor
       #colony resources
       self.ore = ore
       self.food = food
       self.energy = energy
       self.science = science
       self.lifeSupport = lifeSupport
       self.funds = funds
       #colony structures
       self.habitat = habitat
       self.solarPanel = solarPanel
       self.mine = mine
       self.farm = farm
       self.atmosphericUnit = atmosphereicUnit