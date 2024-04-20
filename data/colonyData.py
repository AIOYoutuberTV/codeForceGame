from colonyDataTemplate import *
import json

#define resources
ore = resource("Ore",500)
food = resource("Food",500)
energy = resource("Electric Charge",500)
science = resource("Research Points",0)
lifeSupport = resource("Life Support Intregity (%)",100)
funds = fund("Funds (Millions)",500)

#define structures
solarPanel = structure(0,{energy:15},{},{funds:3,ore:5},5)