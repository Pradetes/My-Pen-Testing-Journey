class TareasPendientes:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append({"descripcion": tarea, "completada": False})

    def marcar_completada(self, posicion):
        try:
            self.tareas[posicion]["completada"] = True
        except IndexError:
            print("La posición ingresada no es válida.")

    def mostrar_tareas(self):
        if self.tareas:
            for i, tarea in enumerate(self.tareas):
                estado = "Completada" if tarea["completada"] else "Pendiente"
                print(f"{i + 1}. {tarea['descripcion']} - {estado}")
        else:
            print("No hay tareas pendientes.")

    def eliminar_tarea(self, posicion):
        try:
            del self.tareas[posicion]
        except IndexError:
            print("La posición ingresada no es válida.")


def main():
    print("- Comencemos por el comienzo, bienvenido al Gestor de Tareas -")
    print("--------------------------------------------------------------")
    lista_tareas = TareasPendientes()

    while True:
        print("\n1. Agregue una nueva tarea: ")
        print()
        print("2. Dar por finalizada una tarea:" )
        print()
        print("3. Mostrar el listado de tareas: ")
        print()
        print("4. Eliminar una tarea")
        print()
        print("5. Salir del programa")
        print()

        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == "1":
            nueva_tarea = input("Ingrese la nueva tarea: ")
            lista_tareas.agregar_tarea(nueva_tarea)
        elif opcion == "2":
            posicion = int(input("Ingrese la posición de la tarea que quiera marcar como completada: ")) - 1
            lista_tareas.marcar_completada(posicion)
        elif opcion == "3":
            lista_tareas.mostrar_tareas()
        elif opcion == "4":
            posicion = int(input("Ingrese la posición de la tarea que quiera eliminar: ")) - 1
            lista_tareas.eliminar_tarea(posicion)
        elif opcion == "5":
            print("¡Gracias, nos vemos pronto!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido del listado anterior.")


if __name__ == "__main__":
    main()
