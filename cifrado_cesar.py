class CifradoCesar:
    def __init__(self):
        self.alfabeto = "abcdefghijklmnñopqrstuvwxyz"

    def codificar_decodificar(self):
        print(
            """
        Programa para cifrar texto con el algoritmo César
                    (alfabeto español)
        
        """
        )
        self.codificado = []

        if self.definir_modo() == "d":
            self.rotacion = -int(input("Ingrese la clave de rotación: "))
        else:
            self.rotacion = int(input("Ingrese la clave de rotación: "))

        self.texto = input("Ingrese el mensaje: ").lower()
        self.aux_codificar = [None] * len(self.texto)
        self.aux = self.rotacion
        self.contador = 0

        for i, v in enumerate(self.texto):
            if v in self.alfabeto:
                self.aux += self.alfabeto.index(v)
                if self.aux < len(self.alfabeto):
                    self.aux_codificar.insert(i, self.alfabeto[self.aux])
                else:
                    self.contador += 1
                    self.aux_codificar.insert(i, self.alfabeto[self.contador])
                self.aux = self.rotacion
            else:
                self.aux_codificar[i] = v

        self.codificado = "".join([i for i in self.aux_codificar if i != None])
        return self.codificado.capitalize()

    def definir_modo(self):
        while True:
            print("¿Quiere encriptar o desencriptar?")
            self.modo = input().lower()
            if self.modo == "e" or self.modo == "d":
                return self.modo
            else:
                print(
                    f"""
                      Ingrese 'e' para encriptar,
                      Ingrese 'd' para desencriptar
                      """
                )


cifrar = CifradoCesar()

print(cifrar.codificar_decodificar())
