data_angka = [1,5,2,3]
print(data_angka)

# kumpulan data string
data_string = ["ucup", "siunyil", "ogah"]
print(data_string)

# Kumpulan data boolean
data_boolean = [True, False, True, True]
print(data_boolean)

# Kumpulan Campuran
data_campuran = [1,"ote-ote", 2, "cireng", "risoles", 3]
print(data_campuran)
               
## LIST
data_range = range(0,10)
print(data_range)
data_list = list(range(0,10))
print(data_list)

list_pake_for = [i**2 for i in range(0,10)]
print(list_pake_for)

list_pake_for_if = [i for i in range (0,10) if i != 5]
print(list_pake_for_if)

class Ulang:
        def __init__(self) -> None:
                pass
i = 0  

print(f"Data sebelum ditambah = {data_string}")

data_string.insert(1,"Asep")
print(f"Data sesudah ditambah = {data_string}")


data_string.append("Jajang")
print(f"Data setelah ditambah lagi = {data_string}")

data_baru = ["Ujang", "Usep", "Dadang"]
data_string.extend(data_baru)
print(f"data gabungan = {data_string}")

data_string[2] = "Mamang"
print(f"Data setelah dirubah = {data_string}")

data_string.remove("Ujang")
print(f"data remove = {data_string}")

data_string.pop()
print(f"data akhir = {data_string}")

data_0 = data_string[0]
for i in range(len(data_0)+1):
        
        print(f"Data ke {i} adalah {data_string[i]}")
        i += 1

   