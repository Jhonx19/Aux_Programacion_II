class Anime:
    def __init__(self, nombre, genero, nroEpisodios):
        self.nombre = nombre
        self.genero = genero
        self.nroEpisodios = nroEpisodios
        self.episodios = []

    def agregar_episodio(self, episodio):
        self.episodios.append(episodio)

    def __str__(self):
        return f"Anime: {self.nombre} | Género: {self.genero} | N° Episodios: {self.nroEpisodios}"


class Televisor:
    def __init__(self, marca, resolucion, tipo):
        self.marca = marca
        self.resolucion = resolucion
        self.tipo = tipo

    def __str__(self):
        return f"Televisor Marca: {self.marca} | Resolución: {self.resolucion}p | Tipo: {self.tipo}"


class Instrumento:
    def __init__(self, nombre, material, tipo):
        self.nombre = nombre
        self.material = material
        self.tipo = tipo

    
    def get_nombre(self):
        return self.nombre

    def get_material(self):
        return self.material

    def get_tipo(self):
        return self.tipo

    
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_material(self, material):
        self.material = material

    def set_tipo(self, tipo):
        self.tipo = tipo

    def __str__(self):
        return f"Instrumento: {self.nombre} | Material: {self.material} | Tipo: {self.tipo}"


#CLASE PRINCIPAL
if __name__ == "_main_":

    # Crear 2 objetos Anime
    anime1 = Anime("Naruto", "Acción", 220)
    anime2 = Anime("Death Note", "Suspenso", 37)

    # Crear 2 objetos Televisor
    tv1 = Televisor("Samsung", 1080, "LED")
    tv2 = Televisor("LG", 2160, "OLED")

    # Crear 2 objetos Instrumentos
    inst1 = Instrumento("Guitarra", "Madera", "Cuerda")
    inst2 = Instrumento("Flauta", "Metal", "Aire")

    # Mostrar información
    print("===== ANIMES =====")
    print(anime1)
    print(anime2)

    print("\n===== TELEVISORES =====")
    print(tv1)
    print(tv2)

    print("\n===== INSTRUMENTOS =====")
    print(inst1)
    print(inst2)