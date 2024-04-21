import os
import resource

def splash():
    with open('interface/resource/splashScreren.txt',"rb") as file:
        fileContent = file.read()
    i=0
    file.close()
    return fileContent.decode()