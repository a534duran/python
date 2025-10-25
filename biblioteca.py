import json

# ------------------ Clase Autor ------------------
class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f"{self.nombre} ({self.nacionalidad})"


# ------------------ Clase Libro ------------------
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self._disponible = True

    def prestar(self):
        if not self._disponible:
            raise Exception("El libro no está disponible.")
        self._disponible = False

    def devolver(self):
        self._disponible = True

    def disponible(self):
        return self._disponible

    def __str__(self):
        estado = "Disponible" if self._disponible else "Prestado"
        return f"{self.titulo} - {self.autor.nombre} ({estado})"


# ------------------ Clase Usuario ------------------
class Usuario:
    def __init__(self, nombre, numero_usuario):
        self.nombre = nombre
        self.numero_usuario = numero_usuario
        self._libros_prestados = []

    def puede_prestar(self):
        return len(self._libros_prestados) < 3  # límite de préstamos

    def agregar_libro(self, libro):
        if self.puede_prestar():
            self._libros_prestados.append(libro)
        else:
            raise Exception("Ha alcanzado el límite de préstamos.")

    def devolver_libro(self, libro):
        if libro in self._libros_prestados:
            self._libros_prestados.remove(libro)
        else:
            raise Exception("El libro no pertenece a este usuario.")

    def mostrar_informacion(self):
        return f"Usuario: {self.nombre} | Libros prestados: {len(self._libros_prestados)}"

    def __str__(self):
        return self.mostrar_informacion()


# ------------------ Clase UsuarioPremium (Herencia y Polimorfismo) ------------------
class UsuarioPremium(Usuario):
    def puede_prestar(self):
        return len(self._libros_prestados) < 6  # límite mayor

    def mostrar_informacion(self):
        return f"Usuario PREMIUM: {self.nombre} | Libros prestados: {len(self._libros_prestados)}"


# ------------------ Clase Biblioteca ------------------
class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def registrar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

    def prestar_libro(self, titulo, numero_usuario):
        libro = self.buscar_libro(titulo)
        usuario = next((u for u in self.usuarios if u.numero_usuario == numero_usuario), None)

        if not libro:
            raise Exception("Libro no encontrado.")
        if not usuario:
            raise Exception("Usuario no encontrado.")

        if not libro.disponible():
            raise Exception("El libro ya está prestado.")
        usuario.agregar_libro(libro)
        libro.prestar()

    def devolver_libro(self, titulo, numero_usuario):
        libro = self.buscar_libro(titulo)
        usuario = next((u for u in self.usuarios if u.numero_usuario == numero_usuario), None)

        if libro and usuario:
            usuario.devolver_libro(libro)
            libro.devolver()
        else:
            raise Exception("Datos incorrectos para devolución.")

    def listar_libros_disponibles(self):
        return [libro for libro in self.libros if libro.disponible()]

    def guardar_datos(self, ruta):
        data = {
            "libros": [
                {"titulo": l.titulo, "autor": l.autor.nombre, "isbn": l.isbn, "disponible": l._disponible}
                for l in self.libros
            ],
            "usuarios": [
                {"nombre": u.nombre, "numero_usuario": u.numero_usuario, "prestados": [l.titulo for l in u._libros_prestados]}
                for u in self.usuarios
            ],
        }
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def cargar_datos(self, ruta):
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                data = json.load(f)
                # En este ejemplo, solo mostramos los datos cargados
                print("Datos cargados:", data)
        except FileNotFoundError:
            print("Archivo no encontrado, comenzando con base vacía.")


# ------------------ Prueba del Sistema ------------------
if __name__ == "__main__":
    biblioteca = Biblioteca()

    autor1 = Autor("Gabriel García Márquez", "Colombia")
    autor2 = Autor("Jane Austen", "Reino Unido")

    libro1 = Libro("Cien Años de Soledad", autor1, "001")
    libro2 = Libro("Orgullo y Prejuicio", autor2, "002")

    usuario1 = Usuario("Carlos Pérez", 1)
    usuario2 = UsuarioPremium("María López", 2)

    biblioteca.registrar_libro(libro1)
    biblioteca.registrar_libro(libro2)
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    try:
        biblioteca.prestar_libro("Cien Años de Soledad", 2)
        biblioteca.prestar_libro("Orgullo y Prejuicio", 1)
    except Exception as e:
        print("Error:", e)

    for u in biblioteca.usuarios:
        print(u)

    print("\nLibros disponibles:")
    for l in biblioteca.listar_libros_disponibles():
        print("-", l)

    biblioteca.guardar_datos("biblioteca.json")
