#Program konversi stauan temperatur

#program konversi Celcius ke Satuan lain
print ("\nPROGRAM KONVERSI TEMPERATUR \n")


celcius = float(input('Masukkan Suhu dalam celcius:'))
print("Suhu adalah ",celcius,"Celcius")



# REAMUR
reamur = (4/5) * celcius
print("Suhu adalah ",reamur,"Celcius")

#Fahrenheit
fahr = ((9/5) * celcius) + 32
print("Suhu adalah ",fahr,"Celcius")

#Kelvin
kelvin = celcius + 273
print("Suhu adalah ",kelvin,"Celcius")