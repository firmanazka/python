''''
nama_lengkap = input("Masukkan Nama Lengkap Anda : ")
d = "d"
status = d in nama_lengkap
panjang = len(nama_lengkap)
print("huruf "+ d +" ada di " + nama_lengkap + " = " + str(status))
print("Panjang nama = " + nama_lengkap + " adalah = " + str(panjang))


nama_lengkap = input("Masukkan Nama Lengkap Anda : ")
d = "d"
status = d not in nama_lengkap
print("huruf "+ d +" tidak ada di " + nama_lengkap + " = " + str(status))


print("ïndekx ke - 0 adalah : " + nama_lengkap[0])
print("ïndekx ke - 1 adalah : " + nama_lengkap[1])
print("ïndekx ke - 2 adalah : " + nama_lengkap[2])
print("ïndekx ke - 3 adalah : " + nama_lengkap[3])
print("ïndekx ke - 0 sampai 3 adalah : " + nama_lengkap[0:3])
print("ïndekx ke - 0 sampai 3 adalah : " + nama_lengkap[0:3])

ascii_code = ord(" ")
print("Ascii vode untuk spasi adalah " + str(ascii_code))
'''

''''
kalimat= "sujiwo sutejo diryodiningrat"
jumlah = kalimat.count("o")
print("Jumlah huruf o pada kalimat " + kalimat + " adalah " + str(jumlah))
'''''
''''
# Upper and Lower
salam = "asssalaamu alaikum"
print ("normal = " + salam)
salam = salam.lower()
print(salam)
apakah = salam.islower()
print("Apakah tulisan kecil = " + str(apakah))

salam = salam.upper()
print(salam)
apakah = salam.isupper()
print("Apakah tulisan besar = " + str(apakah))

kalimat = "Assalaamualaikum Bro"
cek_start = kalimat.startswith("Assalaamualaikum")
cek_end = kalimat.endswith("Bro")
print("Start = " + str(cek_start))
print("Ending =" + str(cek_end))
'''
pisah = ('satu','dua','tiga')
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan2 = "satuehmduaehmtiga"
print(gabungan2.split('ehm'))

kanan = "kanan".rjust(10)
kiri = "kiri".ljust(10)
tengah = "kiri".center(10)
print("'" + kanan + "'")
print("'" + kiri + "'")
print("'" + tengah + "'")
print('')





