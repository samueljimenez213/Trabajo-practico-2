from models import Pila, Cola

pila = Pila(5)
cola = Cola(5)


def pausa():
    input("\nPresione Enter para continuar...")


def mostrar_resultado(exito, mensaje):
    if exito:
        print(f"✓ {mensaje}")
    else:
        print(f"✗ {mensaje}")


def apilar():
    print("--- APILAR (Push) ---")
    dato = input("Dato a apilar: ").strip()
    if dato == "":
        print("✗ El dato no puede estar vacio")
    else:
        mostrar_resultado(*pila.apilar(dato))
    pausa()


def desapilar():
    print("--- DESAPILAR (Pop) ---")
    mostrar_resultado(*pila.desapilar())
    pausa()


def ver_tope():
    print("--- ELEMENTO SUPERIOR (Peek) ---")
    mostrar_resultado(*pila.ver_tope())
    pausa()


def mostrar_pila():
    print("--- ELEMENTOS DE LA PILA ---")
    if pila.esta_vacia():
        print("La pila esta vacia")
    else:
        for posicion in range(len(pila.mostrar()) - 1, -1, -1):
            print(f"  | {pila.mostrar()[posicion]} |")
        print("  (arriba es el tope)")
    print(f"Elementos: {len(pila.mostrar())} de {pila.capacidad}")
    pausa()

def encolar():
    print("--- ENCOLAR (Enqueue) ---")
    dato = input("Dato a encolar: ").strip()
    if dato == "":
        print("✗ El dato no puede estar vacio")
    else:
        mostrar_resultado(*cola.encolar(dato))
    pausa()


def desencolar():
    print("--- DESENCOLAR (Dequeue) ---")
    mostrar_resultado(*cola.desencolar())
    pausa()


def ver_frente():
    print("--- PRIMER ELEMENTO (Front) ---")
    mostrar_resultado(*cola.ver_frente())
    pausa()


def mostrar_cola():
    print("--- ELEMENTOS DE LA COLA ---")
    if cola.esta_vacia():
        print("La cola esta vacia")
    else:
        texto = ""
        for dato in cola.mostrar():
            texto += f"[{dato}] "
        print(f"  frente -> {texto}<- final")
    print(f"Elementos: {len(cola.mostrar())} de {cola.capacidad}")
    pausa()


MENU_PILA = {
    "1": ("Apilar (Push)", apilar),
    "2": ("Desapilar (Pop)", desapilar),
    "3": ("Ver elemento superior (Peek)", ver_tope),
    "4": ("Mostrar elementos", mostrar_pila),
    "0": ("Volver", None),
}

MENU_COLA = {
    "1": ("Encolar (Enqueue)", encolar),
    "2": ("Desencolar (Dequeue)", desencolar),
    "3": ("Ver primer elemento (Front)", ver_frente),
    "4": ("Mostrar elementos", mostrar_cola),
    "0": ("Volver", None),
}


def ejecutar_menu(titulo, opciones):
    """Un solo bucle para los dos submenus."""
    while True:
        print("\n" + "=" * 40)
        print(f"  {titulo}")
        print("=" * 40)
        for tecla, (texto, _funcion) in opciones.items():
            print(f"  {tecla}. {texto}")
        print()

        tecla = input("Opcion: ").strip()
        if tecla not in opciones:
            print("✗ Opcion no valida")
            pausa()
            continue

        _texto, funcion = opciones[tecla]
        if funcion is None:      
            break
        funcion()


def main():
    while True:
        print("\n" + "=" * 40)
        print("  PILAS Y COLAS")
        print("=" * 40)
        print("  1. Pila (LIFO)")
        print("  2. Cola (FIFO)")
        print("  0. Salir\n")

        tecla = input("Opcion: ").strip()
        if tecla == "1":
            ejecutar_menu("PILA", MENU_PILA)
        elif tecla == "2":
            ejecutar_menu("COLA", MENU_COLA)
        elif tecla == "0":
            print("Hasta luego!")
            break
        else:
            print("✗ Opcion no valida")
            pausa()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")