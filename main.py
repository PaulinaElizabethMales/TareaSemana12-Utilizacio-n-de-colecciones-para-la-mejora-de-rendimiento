from modelos.libro import Libro
from modelos.usuario import Usuario
from servicios.biblioteca_servicio import BibliotecaServicio

def menu():
    servicio = BibliotecaServicio()

    while True:
        print("/----------------------------------")
        print("/--- Bienvenido a la biblioteca ---")
        print("/----------------------------------")
        print("[1] Añadir libro")
        print("[2] Quitar libro")
        print("[3] Registrar usuario")
        print("[4] Dar de baja usuario")
        print("[5] Prestar libro")
        print("[6] Devolver libro")
        print("[7] Buscar libro")
        print("[8] Listar libros prestados")
        print("[0] Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            libro = Libro(titulo, autor, categoria, isbn)
            servicio.agregar_libro(libro)

        elif opcion == "2":
            isbn = input("ISBN del libro a quitar: ")
            servicio.quitar_libro(isbn)

        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            user_id = input("ID único: ")
            usuario = Usuario(nombre, user_id)
            servicio.registrar_usuario(usuario)

        elif opcion == "4":
            user_id = input("ID del usuario a dar de baja: ")
            servicio.dar_baja_usuario(user_id)

        elif opcion == "5":
            user_id = input("ID del usuario: ")
            isbn = input("ISBN del libro: ")
            servicio.prestar_libro(user_id, isbn)

        elif opcion == "6":
            user_id = input("ID del usuario: ")
            isbn = input("ISBN del libro: ")
            servicio.devolver_libro(user_id, isbn)

        elif opcion == "7":
            print("-----------------------------")
            print("/--- Submenú de búsqueda ---/")
            print("-----------------------------")
            print("1. Buscar por título")
            print("2. Buscar por autor")
            print("3. Buscar por categoría")
            subop = input("Seleccione una opción: ")

            if subop == "1":
                titulo = input("Título: ")
                resultados = servicio.buscar_por_titulo(titulo)
            elif subop == "2":
                autor = input("Autor: ")
                resultados = servicio.buscar_por_autor(autor)
            elif subop == "3":
                categoria = input("Categoría: ")
                resultados = servicio.buscar_por_categoria(categoria)
            else:
                resultados = []

            if resultados:
                for libro in resultados:
                    print(libro)
            else:
                print("No se encontraron resultados.")

        elif opcion == "8":
            user_id = input("ID del usuario: ")
            libros = servicio.listar_libros_prestados(user_id)
            if libros:
                for libro in libros:
                    print(libro)
            else:
                print("No tiene libros prestados.")

        elif opcion == "0":
            print("Gracias vuelva pronto...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()