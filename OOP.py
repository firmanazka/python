class Hero:
    jumlah = 0
    
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.Armor  = inputArmor
        Hero.jumlah += 1
        print("Membuat Hero dengan nama = " + inputName)


hero1 = Hero("sniper", 100, 10, 4)
print(Hero.jumlah)
hero2 = Hero("mirana", 100, 15, 1)
print(Hero.jumlah)
hero3 = Hero("ucup", 100, 100, 0)
print(Hero.jumlah)
''''
print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
'''


''''

hero1 = Hero()
hero2 = Hero()
hero3 = Hero()

hero1.name = "sniper"
hero1.health = 100

hero2.name = "sven"
hero2.health = 200

hero3.name = "ucup"
hero3.health = 1000

print(hero1)
print(hero1.__dict__)
print(hero1.name)

'''