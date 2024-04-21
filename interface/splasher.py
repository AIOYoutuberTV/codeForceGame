def start(): #returns the string of the start screen
    with open('interface/resource/splashScreren.txt',"rb") as file:
        fileContent = file.read()
    i=0
    file.close()
    return fileContent.decode()