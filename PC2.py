cola = []

# Función para encolar (agregar al final)
def encolar(cola, elemento):
    nueva_cola = [0] * (len(cola) + 1)  # Creamos nueva lista con un espacio más
    for i in range(len(cola)):
        nueva_cola[i] = cola[i]          # Copiamos los elementos existentes
    nueva_cola[len(cola)] = elemento     # Agregamos el nuevo elemento al final
    return nueva_cola                    # Retornamos la nueva cola

elemento_eliminado = None
# Función para desencolar (eliminar el primero)
def desencolar(cola):
    global elemento_eliminado
    if len(cola) == 0:
        print("La cola está vacía")
        return cola                      # Retorna la misma cola y None
    
    elemento_eliminado = cola[0]         # Guardamos el primer elemento

    nueva_cola = [0] * (len(cola) - 1)   # Nueva lista con un espacio menos
    for i in range(1, len(cola)):
        nueva_cola[i - 1] = cola[i]      # Desplazamos todos a la izquierda
    return nueva_cola                    # Retornamos la cola actualizada

# Función para mostrar el elemento desencolado
def mostrarElementoEliminado():
    return elemento_eliminado

# Encolamos elementos
cola = encolar(cola, "A")
cola = encolar(cola, "B")
cola = encolar(cola, "C")
print("Cola después de encolar:", cola)
# Desencolamos un elemento
cola = desencolar(cola)
print("Elemento desencolado:", mostrarElementoEliminado())
print("Cola actual:", cola)
# Encolamos otro elemento
cola = encolar(cola, "D")
print("Cola final:", cola)
