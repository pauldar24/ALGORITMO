class Nodo:
    def _init_(self, url, titulo, hora):
        self.url = url
        self.titulo = titulo
        self.hora = hora
        self.sig = None
        self.ant = None

class ListaDoble:
    def _init_(self):
        self.inicio = None
        self.fin = None
    
    def agregarFinal(self, url, titulo, hora):
        nuevo = Nodo(url, titulo, hora)
        if(self.inicio is None):
            self.inicio = nuevo
            self.fin = nuevo
        else:
            self.fin.sig = nuevo
            nuevo.ant = self.fin
            self.fin = nuevo
    
    def mostrarLista(self):
        p = self.inicio
        while p:
            print(p.url, p.titulo, p.hora, end=" <-> ")
            p = p.sig

    def retroceder(self):
        p = self.fin
        print(f"\nPágina actual: {p.url, p.titulo, p.hora}")
        r = input("Desea retroceder? [SÍ(s)/NO(n)]: ").lower()
        while p and r=="s":
            if p.ant:
                print(f"\nEl URL anterior: {p.ant.url, p.ant.titulo, p.ant.hora}")
            else:
                print("\nYa no hay páginas hacia atrás")
            p = p.ant
            r = input("Desea seguir retrocediendo? [SÍ(s)/NO(n)]: ").lower()

    def avanzar(self):
        p = self.inicio
        print(f"\nURL actual: {p.url, p.titulo, p.hora}")
        r= input("Desea avanzar? [SÍ(s)/NO(n)]: ").lower()
        while p and r=="s":
            if p.sig:
                print(f"\nSiguiente url: {p.sig.url, p.sig.titulo, p.sig.hora}")
            else:
                print("\nYa no hay más páginas hacia adelante")
            p = p.sig
            r =input("Seguir avanzando? [SÍ(s)/NO(n)]: ").lower()
    
    def eliminar(self, urlBscdo):
        p = self.inicio
        while p:
            if(p.url == urlBscdo):
                if(p==self.inicio):  # Si está al inicio
                    self.inicio = p.sig
                    if self.inicio:  #Si hay un siguiente nodo
                        self.inicio.ant = None
                    else:
                        self.fin = None  # La lista quedó vacía
                elif(p==self.fin):  # Está al final
                    self.fin = p.ant
                    if self.fin:
                        self.fin.sig = None
                else:  # Está en el medio
                    p.ant.sig = p.sig
                    p.sig.ant = p.sig
                print(f"Se eliminó {urlBscdo}")
            p = p.sig
            return
        print(f"No se encontró {urlBscdo}")

    def buscar(self, urlBscr):
        p = self.inicio
        while p:
            if(p.url == urlBscr):
                print("Se encontró el URL!!!", p.url)
                break
            else:
                p = p.sig
        return

#---------------------------------------------------------------------
lisD = ListaDoble()

def poblar():
    r = "s"
    while r=="s":
        print()
        url = input("URL: ")
        titulo = input("Título: ")
        hora = input("Hora: ")
        lisD.agregarFinal(url, titulo, hora)

        r = input("\nAgregar más al historial? [SÍ(s)/NO(n]: ").lower()

def procesoBuscar():
    urlBscr = input("\nQué URL desea buscar: ")
    lisD.buscar(urlBscr)

def procesoEliminar():
    urlEliminar = input("\nIngrese el URL que desea eliminar: ")
    lisD.eliminar(urlEliminar)

# Agregando el historial ya registrado
lisD.agregarFinal("google.com", "Google", "10:00 AM")
lisD.agregarFinal("wikipedia.org", "Wikipedia", "10:05 AM")
lisD.agregarFinal("github.com", "Github", "10:10 AM")
lisD.agregarFinal("stackoverflow.com", "Stack Overflow", "10:15 AM")

#Empezar a agregar páginas
poblar()

#Mostrar el historial
lisD.mostrarLista()
print()

#Retroceder en el historial
lisD.retroceder()
print()

#Avanzar en el historial
lisD.avanzar()

#Buscar y eliminar
procesoBuscar()

#Eliminar
procesoEliminar()
print()
lisD.mostrarLista()
