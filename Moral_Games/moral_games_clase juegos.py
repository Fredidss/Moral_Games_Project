class Videojuego:
    def __init__(self, titulo, plataforma, precio, cantidad, genero):
        self.titulo = titulo
        self.plataforma = plataforma
        self.precio = precio
        self.cantidad = cantidad
        self.genero = genero


class VideojuegoConRequisitos(Videojuego):
    def __init__(self, titulo, plataforma, precio, cantidad, genero, requisitos_minimos=None):
        super().__init__(titulo, plataforma, precio, cantidad, genero)
        if plataforma == "PC":
            self.requisitos_minimos = requisitos_minimos
        else:
            self.requisitos_minimos = None


class VideojuegoConClasficacion(Videojuego):
    def __init__(self, titulo, plataforma, precio, cantidad, genero, clasificacion=None):
        super().__init__(titulo, plataforma, precio, cantidad, genero)
        if plataforma in ["play station 5", "play station 2", "Xbox ONE"]:
            self.clasificacion = clasificacion
        else:
            self.clasificacion = None

       
juego1 = Videojuego("NFS Most Wanted", "Play Station 2", "$200", "21", "Autos")
juego2 = Videojuego("FIFA 23", "Play Station 5", "$800", "12", "Deportes")
juego3 = Videojuego("NBA 2K23", "Xbox ONE", "$1300", "8", "Deportes")
juego4 = Videojuego("HALO", "Xbox ONE", "$1600", "14", "FPS")
juego5 = VideojuegoConRequisitos("COD World War II", "PC", "$1500", "12", "FPS", "Procesador Intel Core i5, 8GB RAM, Tarjeta grafica NVIDIA GTX 1050, Disco duro 1TB")
juego6 = Videojuego("ACE COMBAT 5", "Play station 2", "$350", "4", "aviones")


class Tienda:
    def __init__(self):
        self.inventario = []

    def registrar_juego(self, juego):
        self.inventario.append(juego)
        print("Juego registrado exitosamente!")

    def buscar_juego(self, busqueda):
        resultados = []
        for juego in self.inventario:
            if busqueda.lower() in juego.titulo.lower() or busqueda.lower() in juego.genero.lower():
                resultados.append(juego)
        if resultados:
            print("Resultados:")
            for resultado in resultados:
                print(resultado)
        else:
            print("No se encontraron resultados.")

    def comprar_juego(self, juego, cantidad):
        for j in self.inventario:
            if j.titulo == juego.titulo and j.plataforma == juego.plataforma:
                if j.cantidad >= cantidad:
                    j.cantidad -= cantidad
                    precio_total = int(j.precio[1:]) * cantidad
                    print(f"Compra realizada exitosamente! Precio total: ${precio_total}")
                else:
                    print("No hay suficiente stock para realizar la compra.")
                return
        print("El juego seleccionado no se encuentra en el inventario.")

    def calcular_precio(self, lista_juegos):
        precio_total = 0
        for juego in lista_juegos:
            for j in self.inventario:
                if j.titulo == juego.titulo and j.plataforma == juego.plataforma:
                    precio_total += int(j.precio[1:]) * juego.cantidad
                break
        else:
            print(f"No se encontró el juego '{juego.titulo}' para la plataforma '{juego.plataforma}' en el inventario.")
        return precio_total