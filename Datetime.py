import datetime as dt

hari_ini = dt.date.today()
tanggal = dt.date(2005,10,10)
print(f"Hari ini adalah hari = {hari_ini:%A}")
print(tanggal)

print(hari_ini)
print("Silahkan masukkan tanggal, \nbulan dan tahun lahir")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(tanggal_lahir)
print(f"Tanggal lahir anda adalah = {tanggal_lahir}")

umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
print(f'umur Anda adalah {umur_tahun} tahun')
