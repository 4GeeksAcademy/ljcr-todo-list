import csv


tasks = []


def add_one_task(title):
	clean_title = title.strip() if isinstance(title, str) else ""
	if not clean_title:
		print("Error: no puedes agregar una tarea vacia.")
		return False

	tasks.append(clean_title)
	return True


def print_list():
	print("\nLISTA DE TAREAS")
	print("-" * 40)

	if not tasks:
		print("(sin tareas)")
		print("-" * 40)
		return

	for index, task in enumerate(tasks, start=1):
		print(f"{index:>2}. [ ] {task}")

	print("-" * 40)


def delete_task(number_to_delete):
    try:
        task_index = int(number_to_delete) - 1
    except (TypeError, ValueError):
        print("Error: debes ingresar un numero valido.")
        return False

    if task_index < 0 or task_index >= len(tasks):
        print("Error: el numero de tarea esta fuera de rango.")
        return False

    tasks.pop(task_index)
    return True


def save_todos():
    with open("todos.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        for task in tasks:
            writer.writerow([task])


def load_todos():
    try:
        with open("todos.csv", "r", newline="", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            tasks.clear()
            for row in reader:
                if row:
                    tasks.append(row[0])
    except FileNotFoundError:
        tasks.clear()


def main():
    # Carga las tareas existentes al iniciar la aplicacion.
    load_todos()

    while True:
        print("\n--- MENU TODO ---")
        print("1. Agregar")
        print("2. Listar")
        print("3. Eliminar")
        print("4. Salir")

        # Captura la opcion elegida por el usuario.
        option = input("Selecciona una opcion: ").strip()

        if option == "1":
            title = input("Escribe la tarea: ").strip()
            if add_one_task(title):
                save_todos()
                print("Tarea agregada.")
        elif option == "2":
            print_list()
        elif option == "3":
            number_to_delete = input("Numero de tarea a eliminar: ").strip()
            if delete_task(number_to_delete):
                save_todos()
                print("Tarea eliminada.")
        elif option == "4":
            print("Hasta luego.")
            break
        else:
            print("Opcion invalida. Intenta de nuevo.")


if __name__ == "__main__":
    main()