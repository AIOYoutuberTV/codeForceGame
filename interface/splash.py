import os
import resource

def splash():
    with open('interface/resource/splashScreren.txt',"rt") as file:
        fileContent = file.readlines()
    i=0
    while i<len(fileContent):
        print(fileContent[i])
        i+=1
    file.close()

splash()