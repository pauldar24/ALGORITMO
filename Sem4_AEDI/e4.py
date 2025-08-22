pilaFia = []
pilaFia2 = []

# Push inicial
for i in range(1, 16):
    pilaFia.append(i)

print("Pila inicial:", pilaFia)

pilaFia2.append(pilaFia.pop(2)) # Elimina el 3er elemento y lo agrega en la pilaFia2
pilaFia2.append(pilaFia.pop(6)) # Elimina el 7mo elemento y lo agrega en la pilaFia2

print("Pila después de eliminar el número:", pilaFia)
print("Elementos guardados temporalmente:", pilaFia2)


print("Pila restaurada (sin el número eliminado):", pilaFia)