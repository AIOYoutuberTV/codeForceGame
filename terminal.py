from data.colonyDataTemplate import version

#Terminal-like input
UserName = "Admin"
SysName = "Colony189"
Path = "~"
def term():
    endTurn = False
    while not endTurn:
        print(UserName+"@"+SysName+":"+Path,end="$ ")
        cmd = input().lower()
        print("Inputted>",cmd)
        if cmd == "signoff":
            endTurn = True
        if cmd == "help":
            print("""version -> operating system's version
help -> help with commands
signoff -> logs off to another day""")
        if cmd == "version":
            print("Colony Supervisor OS v."+version)

# Main game loop

while True:
    #Let User do thier turn
    #Then "tick" the game
    term()
    print("Ending Turn")