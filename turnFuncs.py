from data.colonyTemplate import *
from data.colonyData import *

#Function to run the structures.
def structureRun(inflow:structure):
	#calculate the gains
	productionKeys = list(inflow.production.keys())
	i = 0
	while i < len(inflow.production):
		match productionKeys[i].name:
			case 'Life Support Intregity (%)':
				if lifeSupport.count + inflow.production[lifeSupport]*inflow.count <= 100:
					lifeSupport.count += inflow.production[lifeSupport]*inflow.count
				else:
					lifeSupport.count = 100
				i+=1
				#return "Life Support is now:"+str(lifeSupport.count)+"%"
			case _:
				productionKeys[i].get(inflow.production[productionKeys[i]]*inflow.count) # wtf use strings for god's
				i+=1
				#return "Ore is now:"+str(ore.count)
	del(i)

	#Calculate the drains
	consumptionKeys = list(inflow.consumption.keys())
	i = 0
	while i < len(inflow.consumption):
		match consumptionKeys[i].name:
			case 'Life Support Intregity (%)':
				if lifeSupport.count - inflow.consumption[lifeSupport]*inflow.count >= 0: #Greater or equal than exists, WHY WERE YOU USING !=
					lifeSupport.count -= inflow.consumption[lifeSupport]*inflow.count
				else:
					lifeSupport.count = 0
				i+=1
			case _:
				consumptionKeys[i].spend(inflow.consumption[consumptionKeys[i]]*inflow.count)
				i+=1
	del(i)

def structureBuild(inflow:structure,howMany:int=1):
	totalCost = howMany * inflow.cost
	if totalCost > funds.count:
		return "Error: Not sufficient funds."
	else:
		funds.spend(howMany*inflow.cost)
		inflow.count += howMany
		return "Builing successful! You now have "+str(howMany)+" more "+str(inflow.name)

def resourceSell(inflow:resource,howMuch:int=1):
	if howMuch > inflow.count:
		return "Error: Not sufficient resources."
	else:
		funds.get(inflow.pricePerUnit*howMuch)
		inflow.spend(howMuch)
		return "Selling sucessful! You now have "+str(inflow.pricePerUnit*howMuch)+" more funds!"