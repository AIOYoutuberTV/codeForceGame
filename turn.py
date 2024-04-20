from data.colonyDataTemplate import *
from data.colonyTemplate import *
from data.colonyData import *

def structureRun(inflow:structure=solarPanel):
    #calculate the gains
    productionKeys = list(inflow.production.keys())
    i = 0
    while i < len(inflow.production):
        match productionKeys[i].name:
            case 'Ore':
                ore.get(inflow.production[ore]*inflow.count)
                i+=1
            case 'Food':
                food.get(inflow.production[food]*inflow.count)
                i+=1
            case 'Electric Charge':
                energy.get(inflow.production[energy]*inflow.count)
                i+=1
            case 'Research Points':
                science.get(inflow.production[science]*inflow.count)
                i+=1
            case 'Life Support Intregity (%)':
                lifeSupport.get(inflow.production[lifeSupport]*inflow.count)
                i+=1
            case 'Funds (M€)':
                funds.get(inflow.production[fund]*inflow.count)
                i+=1
    del(i)

    #Calculate the drains
    consumptionKeys = list(inflow.consumption.keys())
    i = 0
    while i < len(inflow.consumption):
        match consumptionKeys[i].name:
            case 'Ore':
                ore.spend(inflow.consumption[ore]*inflow.count)
                i+=1
            case 'Food':
                food.spend(inflow.consumption[food]*inflow.count)
                i+=1
            case 'Electric Charge':
                energy.spend(inflow.consumption[energy]*inflow.count)
                i+=1
            case 'Research Points':
                science.spend(inflow.consumption[science]*inflow.count)
                i+=1
            case 'Life Support Intregity (%)':
                lifeSupport.spend(inflow.consumption[lifeSupport]*inflow.count)
                i+=1
            case 'Funds (M€)':
                funds.spend(inflow.consumption[fund]*inflow.count)
                i+=1
    del(i)