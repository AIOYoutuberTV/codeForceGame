from data.colonyDataTemplate import *
from data.colonyTemplate import *
from data.colonyData import *
from data.colony import *
import interface.terminal as term
from interface.tui import *
import turnFuncs as Turns
TUI.__init__()
term.bind("sell",lambda x,y: Turns.resourceSell(resources[x],y) if (x in resources) else "Error: Resource Doesnt Exist")
term.bind("buy",lambda x,y: Turns.structureBuild(structures[x],y) if (x in structures) else "Error: Resource Doesnt Exist")

for key in resources:
    res = resources[key]
    TUI.addInfo(res.getType(),res)

while True:
    #Run the structures here
    for key in structures:
        Turns.structureRun(structures[key])
    
    
    
    #Let User do thier turn
    #Then "tick" the game
    #Terminal handling
    term.term()
    TUI.print("Ending Turn")
    TUI.render()