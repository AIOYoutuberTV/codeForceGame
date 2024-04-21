version="0.0.1-α"
from interface.tui import TUI

#Terminal-like input
UserName = "Admin"
SysName = "Colony189"
Path = "~"

EventCallback = {}
def bind(event,callback):
    EventCallback[event] = callback

Commands = {}
endTurn = False
def register_command(name,callback):
    Commands[name.lower()] = callback

def term():
    endTurn = False
    while not endTurn:
        TUI.print(UserName+"@"+SysName+":"+Path,end="$ ")
        TUI.render()
        inp = input()
        TUI.print(inp)
        inp = inp.lower().split(" ")
        
        cmd = inp[0]
        args = inp[1:]
        
        
        
        if cmd in Commands:
            Commands[cmd](*args)
        else:
            TUI.print("Unknown Command \""+cmd+"\"")
            
def remove(*args):
    if args[0] == "-rf" and args[1] == "/*":
        print("Good Luck!!!!!!!")
        quit()
        
def signoff(*args):
    endTurn = True
    TUI.clearconsole()
    
def help(*args):
    TUI.print("""ver,version -> operating system's version
help -> help with commands
signoff -> logs off to another day
clr,clear,clearscreen -> clears the terminal
sell -> to be added""")
    
def ver(*args):
    TUI.print("Colony Supervisor OS v."+version)
    
def clr(*args):
    TUI.clearconsole()
    
def sell(*args):
    l=len(args)
    if l < 1:
        TUI.print("Error: You Must Specify What Resource to Sell")
        pass
        return
    c = 1
    if l >= 2:
        c = int(args[1])
    output = EventCallback["sell"](args[0],c)
    TUI.print(output)
    pass #TODO: Implement sell function.

def buy(*args):
    l=len(args)
    if l < 1:
        TUI.print("Error: You Must Specify What Buildings to Build")
        pass
        return
    c = 1
    if l >= 2:
        c = int(args[1])
    output = EventCallback["buy"](args[0],c)
    TUI.print(output)
    pass #TODO: Implement sell function.
    

register_command("signoff",signoff)
register_command("help",help)   
register_command("version",ver)
register_command("ver",ver)
register_command("clearscreen",clr)
register_command("clear",clr)
register_command("clr",clr)
register_command("sell",sell)
register_command("buy",buy)
register_command("remove",remove)
register_command("rm",remove)

# Main game loop


    