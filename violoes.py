from prototype import violao

class violao_classico(violao):
    def __init__(self):
        super().__init__()
        self.material = "Madeira"
        self.numero_cordas = "6"
        self.nivel = "Iniciante"

    def tocar(self):
        print("Tocando violão clássico")

    def afinar(self):
        print("Afinando violão clássico")


class violao_folk(violao):
    def __init__(self):
        super().__init__()
        self.material = "Madeira"
        self.numero_cordas = "6"
        self.nivel = "Intermediario"

    def tocar(self):
        print("Tocando violão folk")

    def afinar(self):
        print("Afinando violão folk")

class violao_flet(violao):
    def __init__(self):
        super().__init__()
        self.material = "Madeira Fina"
        self.numero_cordas = "6"
        self.nivel = "Profissional"

    def tocar(self):
        print("Tocando violão flet")

    def afinar(self):
        print("Afinando violão flet")

class violao_jumbo(violao):
    def __init__(self):
        super().__init__()
        self.material = "Madeira(Arredondado)"
        self.nivel = "Profissional"
        self.numero_cordas = "6"

    def tocar(self):
        print("Tocando violão jumbo")

    def afinar(self):
        print("Afinando violão jumbo")

class violao_7_cordas(violao):
    def __init__(self):
        super().__init__()
        self.material = "Madeira"
        self.numero_cordas = "7"
        self.nivel = "Profissional"

    def tocar(self):
        print("Tocando violão 7 cordas")

    def afinar(self):
        print("Afinando violão 7 cordas")

class violao_12_cordas(violao):
    def __init__(self):
        super().__init__()
        self.material = "Madeira"
        self.numero_cordas = "12"
        self.nivel = "Profissional"

    def tocar(self):
        print("Tocando violão 12 cordas")

    def afinar(self):
        print("Afinando violão 12 cordas")

class violao_zero(violao):
    def __init__(self):
        super().__init__()
        self.material = "Madeira"
        self.numero_cordas = "6"
        self.nivel = "Intermediario"

    def tocar(self):
        print("Tocando violão zero")

    def afinar(self):
        print("Afinando violão zero")

class violao_duplo_zero(violao):
    def __init__(self):
        super().__init__()
        self.material = "Madeira"
        self.numero_cordas = "6"
        self.nivel = "Intermediario"

    def tocar(self):
        print("Tocando violão duplo zero")

    def afinar(self):
        print("Afinando violão duplo zero")

class violao_triplo_zero(violao):
    def __init__(self):
        super().__init__()
        self.material = "Madeira"
        self.numero_cordas = "6"
        self.nivel = "Intermediario"

    def tocar(self):
        print("Tocando violão triplo zero")

    def afinar(self):
        print("Afinando violão triplo zero")
