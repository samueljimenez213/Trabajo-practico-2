class Pila:
    """Pila (Stack): el ultimo que entra es el primero que sale (LIFO)."""

    def __init__(self, capacidad=5):
        self.capacidad = capacidad
        self.lista = []

    def esta_vacia(self):
        return len(self.lista) == 0

    def esta_llena(self):
        return len(self.lista) >= self.capacidad

    def apilar(self, dato):
        if self.esta_llena():
            return False, "La pila esta llena"
        self.lista.append(dato)
        return True, f"Se apilo: {dato}"

    def desapilar(self):
        if self.esta_vacia():
            return False, "La pila esta vacia"
        dato = self.lista.pop()
        return True, f"Se desapilo: {dato}"

    def ver_tope(self):
        if self.esta_vacia():
            return False, "La pila esta vacia"
        return True, f"El elemento superior es: {self.lista[-1]}"

    def mostrar(self):
        return self.lista


class Cola:
    """Cola (Queue): el primero que entra es el primero que sale (FIFO)."""

    def __init__(self, capacidad=5):
        self.capacidad = capacidad
        self.lista = []

    def esta_vacia(self):
        return len(self.lista) == 0

    def esta_llena(self):
        return len(self.lista) >= self.capacidad

    def encolar(self, dato):
        if self.esta_llena():
            return False, "La cola esta llena"
        self.lista.append(dato)
        return True, f"Se encolo: {dato}"

    def desencolar(self):
        if self.esta_vacia():
            return False, "La cola esta vacia"
        dato = self.lista.pop(0)
        return True, f"Se desencolo: {dato}"

    def ver_frente(self):
        if self.esta_vacia():
            return False, "La cola esta vacia"
        return True, f"El primer elemento es: {self.lista[0]}"

    def mostrar(self):
        return self.lista