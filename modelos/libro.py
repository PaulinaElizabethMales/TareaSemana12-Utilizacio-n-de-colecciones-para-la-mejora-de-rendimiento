# Clase Libro: representa un libro en el sistema
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # título y autor como tupla (inmutable)
        self._info = (titulo, autor)
        self._categoria = categoria
        self._isbn = isbn

    @property
    def info(self):
        return self._info

    @property
    def categoria(self):
        return self._categoria

    @property
    def isbn(self):
        return self._isbn

    def __str__(self):
        return f"{self._info[0]} de {self._info[1]} (ISBN: {self._isbn}, Categoría: {self._categoria})"