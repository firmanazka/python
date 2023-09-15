class Hero:
    #private class variable
    __jumlah = 0

    def __init__(self,name) -> None:
        self.__name = name
        Hero.__jumlah +=1

    # method ini hanya berlaku untuk o bjek    
    def getJumlah(self):
        return Hero.__jumlah
    
    def getJumlah1():
        return Hero.__jumlah
    
    @staticmethod
    def getjumlah2():
        return Hero.__jumlah
    
sniper = Hero('sniper')
print(Hero.getjumlah2())
rikimaru = Hero('rikimaru')
print(sniper.getjumlah2())
drowranger = Hero('drowranger')
print(drowranger.getjumlah2())
