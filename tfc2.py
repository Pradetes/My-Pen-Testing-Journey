from colorama import init, Fore
import time

# Inicializar colorama
init(autoreset=True)

class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append({"tarea": tarea, "completada": False})

    def marcar_completada(self, indice):
        try:
            self.tareas[indice]["completada"] = True
        except IndexError:
            print("Error:", Fore.RED + "La tarea especificada no existe")

    def mostrar_tareas(self):
        print("Tareas pendientes:")
        for i, tarea in enumerate(self.tareas):
            estado = "Completada" if tarea["completada"] else "Pendiente"
            estado_color = Fore.GREEN if tarea["completada"] else Fore.RED
            print(f"{i + 1}. {tarea['tarea']} - {estado_color}{estado}")

    def eliminar_tarea(self, indice):
        try:
            del self.tareas[indice]
            print(Fore.GREEN + "Tarea eliminada exitosamente")
        except IndexError:
            print("Error:", Fore.RED + "La tarea especificada no existe")


# Función principal
def main():
    print(Fore.CYAN + "Gestor de Tareas Pendientes")
    print("============================")

    lista = ListaTareas()

    while True:
        print("\n1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tarea = input("Ingrese la nueva tarea: ")
            lista.agregar_tarea(tarea)
        elif opcion == "2":
            lista.mostrar_tareas()
            indice = int(input("Ingrese el número de la tarea completada: ")) - 1
            lista.marcar_completada(indice)
        elif opcion == "3":
            lista.mostrar_tareas()
        elif opcion == "4":
            lista.mostrar_tareas()
            indice = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
            lista.eliminar_tarea(indice)
        elif opcion == "5":
            print(Fore.YELLOW + "¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

    # Agregamos una pausa antes de salir
    time.sleep(2)


if __name__ == "__main__":
    main()
