class ColaFia:
  def __init__(self):
    self.queue = []
    
  def enqueue(self, element):
    self.queue.append(element)

  def dequeue(self):
    if self.isEmpty():
      return "La cola está vacía"
    return self.queue.pop(0)

  def peek(self):
    if self.isEmpty():
      return "La cola está vacía?"
    return self.queue[0]

  def isEmpty(self):
    return len(self.queue) == 0

  def size(self):
    return len(self.queue)

# Create a queue
myColaMatrucula = ColaFia()

myColaMatrucula.enqueue('Aldo')
myColaMatrucula.enqueue('Bianca')
myColaMatrucula.enqueue('Carlos')

print("Cola: ", myColaMatrucula.queue)
print("Primer elemento: ", myColaMatrucula.peek())
print("Elimina: ", myColaMatrucula.dequeue())
print("Cola después de eliminar: ", myColaMatrucula.queue)
print("Está vacía: ", myColaMatrucula.isEmpty())
print("Tamaño: ", myColaMatrucula.size())
