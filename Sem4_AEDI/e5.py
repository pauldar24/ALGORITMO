# Ingresar 20 nombre en una pila y sacar 1 con el concepto de LIFO

pilaFia = []

# Agregando 20 nombres diferentes a la pila
for i in range(4):
    nombre = input("Ingrese un nombre: ")
    pilaFia.append(nombre)

print(f"Pila de nombre: {pilaFia}")

# Sacando por LIFO
pilaFia.pop()
print(f"Pila de nombre sacando 1 elemento por LIFO: {pilaFia}")

# Sacando por FIFO
pilaFia.pop(0)
print(f"Pila de nombre sacando 1 elemento por FIFO: {pilaFia}")
