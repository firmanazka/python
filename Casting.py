#Casting data merubah satu tipe data ke tipe lainnya
print("======Integer=========")
data_int = 9
data_float = float(data_int)
data_bool = bool(data_int)

print ("data = ", data_float, ", type = ", type(data_float))
print ("data = ", data_int, ", type = ", type(data_int))
print ("data = ", data_bool, ", type = ", type(data_bool))

# FLOAT
print("======FLOAT=========")
data_float = 9.7
data_int = int(data_float)
data_bool = bool(data_float)

print ("data = ", data_float, ", type = ", type(data_float))
print ("data = ", data_int, ", type = ", type(data_int))
print ("data = ", data_bool, ", type = ", type(data_bool))


# BOLEAN
print("======BOLEAN=========")
data_bool = True
data_int = int(data_bool)
data_float = float(data_bool)
data_string = str(data_bool)

print ("data = ", data_float, ", type = ", type(data_float))
print ("data = ", data_int, ", type = ", type(data_int))
print ("data = ", data_bool, ", type = ", type(data_bool))
print ("data = ", data_string, ", type = ", type(data_string))

# STRING
print("======String=========")
data_str = "UCUP"
data_int = int(data_string)
data_float = float(data_string)
data_bool = str(data_string)

print ("data = ", data_float, ", type = ", type(data_float))
print ("data = ", data_int, ", type = ", type(data_int))
print ("data = ", data_bool, ", type = ", type(data_bool))
print ("data = ", data_string, ", type = ", type(data_string))