import pickle
from colonyTemplate import *

def saveGameState(input:colony,saveNumber:int):
	saveFile = open("saveFileNo"+str(saveNumber), "w+b")
	pickle.dump(input.__dict__, saveFile)
	saveFile.close()

def loadGameState(saveNumber:int, game:colony):
	saveFile = open("saveFileNo"+str(saveNumber), "rb")
	game = pickle.load(saveFile)
	

game = colony("Utopia Planetia",20)
dict = {game.__getattribute__:game.__getstate__}
print(dict)
#saveGameState(game,1)