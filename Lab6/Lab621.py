# Tupla
miTupla = ("asignacion", "laboratorio", "python")
myit = iter(miTupla)

print(next(myit))
print(next(myit))
print(next(myit))

# Cadena
mystr = "casa"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))

for x in mystr:
    print(x)