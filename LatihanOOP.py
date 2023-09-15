class Hero:

    __jumlah = 0
    def __init__(self,name,health,attPower,armor) -> None:
        self.__name = name
        self.__healthStandar = health
        self.__attPowerStandar = attPower
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandar * self.__level
        self.__attPower = self.__attPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level

        self.__health = self.__healthMax

        Hero.__jumlah += 1
    
    @property
    def info(self):
        return "{} : \n\thealth = {}/{} \n\tlevel = {}\n\tattack = {}\n\tarmor = {}".format(self.__name,self.__health,self.__healthMax,self.__level,self.__attPower,self.__armor)
    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self,addExp):
        self.__exp += addExp
        if (self.__exp >= 100):
            print(self.__name, "now ******level up******")
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthStandar * self.__level
            self.__attPower = self.__attPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level


slardar = Hero('slardar', 100, 5, 10)
print("===================First Spawn==================")
print(slardar.info)

slardar.gainExp = 50
slardar.gainExp = 80
print("===================After Battle==================")
print(slardar.info)
