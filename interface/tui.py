
# import only system from os
import os
 
# define our clear function
def clear():
 
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


class TUI:
    # @param v value of the progress bar
    # @param v maximum value of the progress bar
    # @param progbar_size = 80 progress bar's size
    # @param start = "[" progress bar starting string
    # @param end = "]" progress bar ending string
    # @param fill = "#" progress bar's fill character
    # @param gap = "#" progress bar's space character
    # @return string of the progress bar
    @staticmethod
    def progressBarString(v,maxv,progbar_size = 80,start="[",end="]",fill="#",gap=" "):
        f = v/maxv
        f *= progbar_size
        f = round(f)
        return start+fill*f+gap*(progbar_size-f)+end
    
    @staticmethod
    def __init__():
        TUI.buffer = "\n"
        TUI.information = []
        pass

    @staticmethod
    def addInfo(name,value,maxvalue,hasProgressBar=False):
        TUI.information.append({"name":name,"value":value,"maxvalue":maxvalue,"hasProgressBar":hasProgressBar})
         
    @staticmethod
    def clearInfo():
        TUI.information = []
    
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
                print(TUI.progressBarString(i["value"],i["maxvalue"]))
        
        print("Booting system...")
        print(TUI.buffer.replace("\n","\n# "),end="")