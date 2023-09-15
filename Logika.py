#Project 1
'''

inputUser = float(input("Masukan angka = "))
isKurangDari =  (inputUser<3)
isLebihDari = (inputUser >10)

print (isKurangDari)
print (isLebihDari)

isCorrect = isKurangDari or isLebihDari
print (isCorrect)
'''


inputUser = float(input("Masukan angka = "))
isLebihDari =  (inputUser>3)
isKurangDari = (inputUser <10)

print (isLebihDari)
print (isKurangDari)

isCorrect = isKurangDari and isLebihDari
print (isCorrect)
