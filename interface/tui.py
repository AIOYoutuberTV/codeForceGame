
# import only system from os
from os import system, name
 
# define our clear function
def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

progbar_size = 80 #What does this do? --Kate

class TUI:
    
    @staticmethod
    def __init__(width,height):
        #TUI.width = width
        #TUI.height = height
        TUI.buffer = "\n"
        TUI.information = []

    @staticmethod
    def addInfo(name,value,maxvalue,hasProgressBar=False):
        TUI.information.append({"name":name,"value":value,"maxvalue":maxvalue,"hasProgressBar":hasProgressBar})
         
    
    @staticmethod
    def print(*text,sep=" ",end="\n"):
        t = False #Why, @cj05. Why?
        for i in text:
            if t:
                TUI.buffer+=sep
            TUI.buffer+=i
            t=True
        TUI.buffer+=end
        
    @staticmethod
    def clearconsole():
        TUI.buffer="\n"
    
    @staticmethod
    def render(isclrscr=True):
        if(isclrscr):
            clear()
            
        print("Colony Data")
        
        for i in TUI.information:
            #print(i)
            print(i["name"],i["value"],"/",i["maxvalue"])
            if i["hasProgressBar"]:
                f = i["value"]/i["maxvalue"]
                f *= progbar_size
                f = round(f)
                print("["+"#"*f+" "*(progbar_size-f)+"]")
        
        print("Booting system...")
        print(TUI.buffer.replace("\n","\n# "),end="")