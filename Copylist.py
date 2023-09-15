a = ["Ucup","Untung", "Dudung"]
print(f"a = {a}")

b = a
print(f"b = {b}")

a[1] = "Michael"
b.sort()
print(f"a = {a}")
print(f"a = {b}")

print (f"address a = {hex(id(a))}")
print (f"address b = {hex(id(b))}")

print("membuat list c dengan a.copy")
# print
c = a.copy()
print (f"address b = {hex(id(c))}")