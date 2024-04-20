from data.colonyDataTemplate import *
uuidCounter=0

noAdvisor = advisor("{NONE}","{NONE}","{NONE}","{NONE}",modifier(1))
#define resources
ore = resource("Ore",500)
food = resource("Food",500)
energy = resource("Electric Charge",500)
science = resource("Research Points",0)
lifeSupport = resource("Life Support Intregity (%)",100)
#TODO: When implementing turn, cap LSI at 100.
funds = fund("Funds (M€)",500)

#define structures
solarPanel = structure(0,{energy:15},{},4,5)
mine = structure(1,{ore:15},{lifeSupport:2,energy:5},4,1)
habitat = habitatStructure(2,20,{energy:8,lifeSupport:10},4,1)
farm = structure(3,{food:20},{energy:6,lifeSupport:6},6,1)
atmosphericUnit = structure(4,{lifeSupport:20},{energy:5},5,1)                  