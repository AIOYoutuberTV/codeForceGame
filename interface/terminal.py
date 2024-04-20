#from data.colonyDataTemplate import version
#what
version="0.0.1"
from tui import TUI
TUI.__init__(10,10)
#Terminal-like input
UserName = "Admin"
SysName = "Colony189"
Path = "~"
def term():
    endTurn = False
    while not endTurn:
        TUI.print(UserName+"@"+SysName+":"+Path,end="$ ")
        TUI.render()
        cmd = input()
        TUI.print(cmd)
        cmd = cmd.lower()
        if cmd == "signoff":
            endTurn = True
            TUI.clearconsole()
        elif cmd == "help":
            TUI.print("""version -> operating system's version
help -> help with commands
signoff -> logs off to another day
clear -> clears the terminal""")
        elif cmd == "version":
            TUI.print("Colony Supervisor OS v."+version)
        elif cmd == "clear":
            TUI.clearconsole()
        else:
            TUI.print("Unknown Command")
        

# Main game loop

while True:
    TUI.addInfo("Energy",69,100,True)
    TUI.addInfo("Morale",10,100)
    #Let User do thier turn
    #Then "tick" the game
    term()
    TUI.print("Ending Turn")
    TUI.render()
    