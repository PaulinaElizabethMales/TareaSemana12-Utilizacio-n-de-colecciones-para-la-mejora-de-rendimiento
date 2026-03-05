import os
from modelos.libro import Libro
from modelos.usuario import Usuario

class BibliotecaServicio:
    def __init__(self):
        self._libros = {}  # {ISBN: Libro}
        self._usuarios = {}
        self._ids_usuarios = set()
        self._archivo_libros = "libros.txt"
        self._cargar_libros()

    # --- Gestión de libros ---
    def agregar_libro(self, libro):
        if libro.isbn in self._libros:
            print("Error: Ya existe un libro con ese ISBN.")
            return
        self._libros[libro.isbn] = libro
        self._guardar_libros()
        print("Libro añadido correctamente.")

    def quitar_libro(self, isbn):
        if isbn in self._libros:
            del self._libros[isbn]
            self._guardar_libros()
            print("Libro eliminado.")
        else:
            print("No se encontró el libro con ese ISBN.")

    # --- Gestión de usuarios ---
    def registrar_usuario(self, usuario):
        if usuario.user_id not in self._ids_usuarios:
            self._usuarios[usuario.user_id] = usuario
            self._ids_usuarios.add(usuario.user_id)
            print("Usuario registrado.")
        else:
            print("Ya existe un usuario con ese ID.")

    def dar_baja_usuario(self, user_id):
        if user_id in self._usuarios:
            del self._usuarios[user_id]
            self._ids_usuarios.remove(user_id)
            print("Usuario eliminado.")
        else:
            print("Usuario no encontrado.")

    # --- Préstamos y devoluciones ---
    def prestar_libro(self, user_id, isbn):
        if user_id in self._usuarios and isbn in self._libros:
            usuario = self._usuarios[user_id]
            libro = self._libros[isbn]
            usuario.prestar_libro(libro)
            del self._libros[isbn]
            self._guardar_libros()
            print("Libro prestado.")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, user_id, isbn):
        if user_id in self._usuarios:
            usuario = self._usuarios[user_id]
            usuario.devolver_libro(isbn)
            print("Libro devuelto.")
        else:
            print("Usuario no encontrado.")

    # --- Búsquedas ---
    def buscar_por_titulo(self, titulo):
        return [libro for libro in self._libros.values() if libro.info[0].lower() == titulo.lower()]

    def buscar_por_autor(self, autor):
        return [libro for libro in self._libros.values() if libro.info[1].lower() == autor.lower()]

    def buscar_por_categoria(self, categoria):
        return [libro for libro in self._libros.values() if libro.categoria.lower() == categoria.lower()]

    def listar_libros_prestados(self, user_id):
        if user_id in self._usuarios:
            return self._usuarios[user_id].libros_prestados
        return []

    # --- Persistencia en archivo ---
    def _guardar_libros(self):
        with open(self._archivo_libros, "w", encoding="utf-8") as f:
            for libro in self._libros.values():
                f.write(f"{libro.info[0]};{libro.info[1]};{libro.categoria};{libro.isbn}\n")

    def _cargar_libros(self):
        if os.path.exists(self._archivo_libros):
            with open(self._archivo_libros, "r", encoding="utf-8") as f:
                for linea in f:
                    titulo, autor, categoria, isbn = linea.strip().split(";")
                    libro = Libro(titulo, autor, categoria, isbn)
                    self._libros[isbn] = libro