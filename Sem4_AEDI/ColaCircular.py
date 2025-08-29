class ColaFia:
  def __init__(self, capacidad):
    self.capacidad = capacidad              # Tamaño fijo de la cola
    self.queue = [None] * capacidad         # Lista predefinida con espacios vacíos
    self.front = -1                         # Índice del primer elemento
    self.rear = -1                          # Índice del último elemento

  def enqueue(self, element):
    if (self.rear + 1) % self.capacidad == self.front:
      return "La cola está llena"           # Condición de cola circular llena

    if self.front == -1:
      self.front = self.rear = 0            # Primer elemento insertado
    else:
      self.rear = (self.rear + 1) % self.capacidad  # Avanza circularmente

    self.queue[self.rear] = element         # Inserta el elemento

  def dequeue(self):
    if self.front == -1:
      return "La cola está vacía"

    eliminado = self.queue[self.front]      # Guarda el elemento a eliminar
    self.queue[self.front] = None           # Limpia el espacio

    if self.front == self.rear:
      self.front = self.rear = -1           # Si era el único elemento, cola vacía
    else:
      self.front = (self.front + 1) % self.capacidad  # Avanza circularmente

    return eliminado

  def peek(self):
    if self.front == -1:
      return "La cola está vacía"
    return self.queue[self.front]           # Muestra el primer elemento

  def isEmpty(self):
    return self.front == -1                 # Cola vacía si front está en -1

  def size(self):
    if self.front == -1:
      return 0
    if self.rear >= self.front:
      return self.rear - self.front + 1     # Caso normal
    return self.capacidad - self.front + self.rear + 1  # Caso circular

# Crear cola circular con capacidad fija
myColaMatricula = ColaFia(5)

# Insertamos 5 elementos (cola llena)
myColaMatricula.enqueue('Aldo')
myColaMatricula.enqueue('Bianca')
myColaMatricula.enqueue('Carlos')
myColaMatricula.enqueue('David')
myColaMatricula.enqueue('Maria')

print("Cola llena:", myColaMatricula.queue)

# Eliminamos 2 elementos
print("Elimina:", myColaMatricula.dequeue())
print("Elimina:", myColaMatricula.dequeue())

print("Cola después de eliminar 2:", myColaMatricula.queue)

# Insertamos 2 elementos más
myColaMatricula.enqueue('Elena')
myColaMatricula.enqueue('Fernando')

print("Cola después de insertar 2 más:", myColaMatricula.queue)
print("Front: ", myColaMatricula.peek())
