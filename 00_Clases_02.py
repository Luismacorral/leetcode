class Perro:

    especie = "Canino" #Variable de clase compartida por todos los objetos instanciados

    def __init__(self, name):
        self.name = name #variable de instancia única para cada objeto

        self.trucos = [] #Creamos una lista vacía para cada instancia de perro

    def add_trick(self, truco):
        self.trucos.append(truco)

perro1 = Perro("Trusky")
perro2 = Perro("Toby")

print("El perro {} es de la especie {}".format(str(perro1.name), str(perro1.especie)))
print("El perro {} es de la especie {}".format(str(perro1.name), str(perro1.especie)))

perro1.add_trick("voltereta")
perro1.add_trick("croqueta")
perro1.add_trick("hacerse el muerto")

perro2.add_trick("molinillo")
perro2.add_trick("bailar")
perro2.add_trick("maullar")

print(perro1.trucos)
print(perro2.trucos)

