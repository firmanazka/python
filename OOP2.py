class Hero:
    #class variable
    jumlah_hero = 0
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        #instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1
    #void function, method tanpa return
    def siapa(self):
        print("Namaku adalah = " +self.name)
    #method dengan argumen
    def healthUp(self,up):
        a = int(self.health + up)
    def getHealth(self):
        return self.health
        

hero1 = Hero('sniper', 100, 10, 5)
hero2 = Hero('mario', 90, 5, 10)
hero3 = Hero('mirana', 100, 10, 10)
'''
print(hero1.__dict__)
print(hero2.__dict__)
'''
print ("--------------Nama Hero--------------")
print("1. Sniper")
print("2. Mario")
print("3. Mirana")
#heroInput = input("Masukkan hero ")

hero1.siapa()
hero1.healthUp(10)
print("Kesehatannku sekarang menjadi ",hero1.getHealth())
hero2.siapa()
hero2.healthUp(100)
print("Kesehatannku sekarang menjadi ",hero2.getHealth())


