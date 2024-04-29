#TODO: Finish research

class ResearchTemplate:
    def __init__(self,name,prerequisites,cost) -> None:
        self.name = name
        self.prerequisites = prerequisites
        self.cost = cost
    
    def canUnlock(self,currentProgress):
        for i in self.prerequisites:
            if i not in currentProgress:
                return False
        return True
    def Unlock(self,)