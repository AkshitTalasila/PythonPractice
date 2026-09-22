class Fubar:

    #both combined

    def __init__(self,name="",sides=0,has_spots=False,job_title="",salary =0.0):

        self.name = name
        self.sides = sides
        self.has_spots = has_spots
        self.job_title = job_title
        self.salary = salary



    def setName(self,newName):
       self.name = newName

    def getName(self):
        return self.name

    def setSides(self,newSides):
        self.sides = newSides

    def getSides(self):
        return self.sides

    def setSpots(self,hasSpots:bool):
        self.has_spots = self.has_spots

    def getSpots(self):
        return self.has_spots

    def setJob(self,newJob):
        self.jobTitle = newJob

    def getJob(self):
        return self.getJob

    def setSalary(self,newSal:float):
        self.salary = newSal

    def getSalary(self):
        return self.salary

    def setHours(self,newHours):
        self.hours = newHours

    def getHours(self):
        return self.hours

    
