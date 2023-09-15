class Hero:

    def __init__(self,name,health,atkPwr):
        self.__name = name
        self.__health = health
        self.__attPower = atkPwr

    def getName(self):
        return self.__name
    
    def getHealth(self):
        return self.__health
    
    def diserang(self,serangPower):
        self.__health -= serangPower

earthShaker = Hero('Earthshaker',50,5)
print(earthShaker.__dict__)

# Game Running
#print(earthShaker.__name)
print(earthShaker.getName())

print(earthShaker.getHealth())
earthShaker.diserang(5)
print(earthShaker.getHealth())
#earthShaker.health += 5
