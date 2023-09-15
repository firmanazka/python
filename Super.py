class Hero:
    def __init__(self,name,health) -> None:
        self.name = name
        self.health = health

    def showInfo(self):
        print("{} dengan health {}".format(self.name,self.health))

class Hero_int(Hero):
    def __init__(self, name) -> None:
        super().__init__(name, 100)
        super().showInfo()

class Hero_str(Hero):
    def __init__(self, name) -> None:
        super().__init__(name, 200)
        super().showInfo()

lina = Hero_int('lina')
axe = Hero_int('axe')

print(lina.name, "", lina.health)
print(axe.name, "", axe.health)




        