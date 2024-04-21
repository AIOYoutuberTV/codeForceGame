from data.colonyDataTemplate import *
uuidCounter=0

noAdvisor = advisor("{NONE}","{NONE}","{NONE}","{NONE}",modifier(1))
#define resources
ore = resource(1,"Ore",500,1)
food = resource(2,"Food",500)
energy = resource(3,"Electric Charge",500)
science = resource(4,"Research Points",0)
lifeSupport = resource(5,"Life Support Intregity (%)",100)
resources = {"ore":ore,"food":food,"energy":energy,"science":science,"life support":lifeSupport}
#DONE: When implementing turn, cap LSI at 100... KINDA. It's not exactly perfect.
funds = fund(0,"Funds (M€)",500)

#define structures
solarPanel = structure(0,{energy:15},{},4,5)
mine = structure(1,{ore:15},{lifeSupport:2,energy:5},4,1)
habitat = habitatStructure(2,20,{energy:8,lifeSupport:10},4,1)
farm = structure(3,{food:20},{energy:6,lifeSupport:6},6,1)
atmosphericUnit = structure(4,{lifeSupport:20},{energy:5},5,1)                
structures = {"solar panel":solarPanel,"mine":mine,"habitat":habitat,"farm":farm,"atmospheric unit":atmosphericUnit}