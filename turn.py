from data.colonyDataTemplate import *
from data.colonyTemplate import *
from data.colonyData import *

def calcUse(input:structure):
    
    #calculate the gains
    productionKeys = list(input.production.keys())
    i = 0
    while i < len(input.production):
        match productionKeys[i].name:
            case 'ore':
                ore.get(input.production[ore]*input.count)
                i+=1
            case 'food':
                food.get(input.production[food]*input.count)
                i+=1
            case 'energy':
                energy.get(input.production[energy]*input.count)
                i+=1
            case 'science':
                science.get(input.production[science]*input.count)
                i+=1
            case 'lifeSupport':
                lifeSupport.get(input.production[lifeSupport]*input.count)
                i+=1
            case 'funds':
                funds.get(input.production[fund]*input.count)
                i+=1
    del(i)

    #Calculate the drains
    consumptionKeys = list(input.consumption.keys())
    i = 0
    while i < len(input.consumption):
        match consumptionKeys[i].name:
            case 'ore':
                ore.spend(input.consumption[ore]*input.count)
                i+=1
            case 'food':
                food.spend(input.consumption[food]*input.count)
                i+=1
            case 'energy':
                energy.spend(input.consumption[energy]*input.count)
                i+=1
            case 'science':
                science.spend(input.consumption[science]*input.count)
                i+=1
            case 'lifeSupport':
                lifeSupport.spend(input.consumption[lifeSupport]*input.count)
                i+=1
            case 'funds':
                funds.spend(input.consumption[fund]*input.count)
                i+=1
    del(i)

pass