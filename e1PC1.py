cursos = [
    {"codigo": "MAT101", "nombre": "Matemáticas I", "hora": "08:00"},
    {"codigo": "FIS202", "nombre": "Física II", "hora": "10:30"},
    {"codigo": "PROG305", "nombre": "Programación Avanzada", "hora": "09:15"},
    {"codigo": "HIST110", "nombre": "Historia Universal", "hora": "07:45"},
    {"codigo": "QUIM150", "nombre": "Química General", "hora": "14:00"}
]

# Ordenamiento por Merge Sort
def mergeSort(inicio, fin):
    if(inicio<fin):
        medio = (inicio+fin)//2
        mergeSort(inicio, medio)
        mergeSort(medio+1, fin)
        merge(inicio, medio, fin)

def merge(inicio, medio, fin):
    global cursos
    izq = cursos[inicio:medio+1]
    der = cursos[medio+1:fin+1]
    i = 0
    j = 0
    k = inicio


    # Se compara las horas de izq y der
    while i < len(izq) and j < len(der):
        if izq[i]["hora"] <= der[j]["hora"]:
            cursos[k] = izq[i]
            i +=1
        else:
            cursos[k] = der[j]
            j += 1
        k += 1

    #Copiar los elementos restantes de izq o der
    while i < len(izq):
        cursos[k] = izq[i]
        i += 1
        k+= 1
    while j < len(der):
        cursos[k] = der[j]
        j += 1
        k += 1

# Búsqueda
def buscarCursoPorHora(hora):
    for i in range(len(cursos)):
        if(cursos[i]["hora"] == hora):
            return cursos[i]
    return

def mostrarLista():
    for i in range(len(cursos)):
        print(cursos[i])
#-----------------------------------------------------------------------
print("Cursos sin ordenar: ")
mostrarLista()
print()

mergeSort(0, len(cursos)-1)
print("Cursos ordenados por hora de inicio: ")
mostrarLista()

# Búsqueda de un curso

horaBscr = input("\nIngrese un hora (HH:MM) para encontrar curso: ")
result = buscarCursoPorHora(horaBscr)
if(result):
    print("Curso encontrado: ", result)
else:
    print("No existe un curso a es ahora de inicio")
