from data.colonyDataTemplate import *
uuidCounter=0

noAdvisor = advisor("{NONE}","{NONE}","{NONE}","{NONE}",modifier(1))
#define resources
ore = resource(1,"Ore",500,1)
food = resource(2,"Food",500)
energy = resource(3,"Electric Charge",500)
science = resource(4,"Research Points",0)
lifeSupport = resource(5,"Life Support Intregity (%)",100)
resources = {"ore":ore,"food":food,"energy":energy,"science":science,"life_support":lifeSupport}
#DONE: When implementing turn, cap LSI at 100... KINDA. It's not exactly perfect.
# wdym it doesnt work
funds = fund(0,"Funds (M€)",500)

#define structures
solarPanel = structure("Solar Panel",0,{energy:15},{},4,5)
coal = structure("Coal Power Plant",0,{energy:12000},{lifeSupport:1,ore:5},1000,0)
mine = structure("Mine",1,{ore:15},{lifeSupport:2,energy:5},4,1)
excavator = structure("Excavator",1,{ore:12500},{lifeSupport:20,energy:1000},4000,0)
habitat = habitatStructure("Habitat",2,20,{energy:8,lifeSupport:10},4,1)
farm = structure("Farm",3,{food:20},{energy:6,lifeSupport:6},6,1)
atmosphericUnit = structure("Atmosphere Unit",4,{lifeSupport:20},{energy:5},5,1)                
structures = {"solar_panel":solarPanel,"mine":mine,"habitat":habitat,"farm":farm,"atmospheric_unit":atmosphericUnit,"coal_power_plant":coal,"excavator":excavator}