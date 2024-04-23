from data.colonyDataTemplate import *
from data.colonyTemplate import *
from data.colonyData import *
from data.colony import *
import interface.terminal as term
from interface.tui import *
import turnFuncs as turn
TUI.__init__()
term.bind("sell",lambda x,y: turn.resourceSell(resources[x],y) if (x in resources) else "Error: Resource Doesnt Exist")
term.bind("build",lambda x,y: turn.structureBuild(structures[x],y) if (x in structures) else "Error: Resource Doesnt Exist")

TUI.addInfo("funds",funds)
for key in resources:
    res = resources[key]
    TUI.addInfo(res.getType(),res)

while True:
    #Run the structures here
    for key in structures:
        turn.structureRun(structures[key])
    
    
    
    #Let User do thier turn
    #Then "tick" the game
    #Terminal handling
    term.term()
    TUI.print("Ending Turn")
    TUI.render()