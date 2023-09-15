class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("Show info di class Hero")
        print("{} health: {}".format(
            self.name, self.health))

class Hero_int(Hero):
    def __init__(self, name):
        super().__init__(name, 100)
    def showInfo(self):
        print("Show info di class Hero_int")
        print("{} \n\tTipe: intelligent, \n\thealth: {}".format(self.name,self.health))

class Hero_str(Hero):
    def __init__(self, name):
        super().__init__(name, 200)

lina = Hero_int('lina')
axe = Hero_str('axe')

axe.showInfo()
