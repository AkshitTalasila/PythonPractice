class Thermometer:
    def __init__(self,curretTemp,pastTemp):
        self.currentTemp = curretTemp
        self.pastTemp = pastTemp

    def printCurrent(self):
        print(self.currentTemp)

    def printPast(self):
        print(self.pastTemp)

    def printComprehensive(self):

        print("The temperature now is: "+str(self.getCurrentTemp())+"c")
        print("The temperature a hour ago was:",self.getPastTemp,"c")

    def getCurrentTemp(self)->float:
        return self.currentTemp

    def getPastTemp(self)->float:
        return self.pastTemp


my_therm = Thermometer(20,56)
my_therm.printCurrent()
my_therm.printPast()
my_therm.printComprehensive()
print(my_therm.getCurrentTemp())
print(my_therm.getPastTemp())