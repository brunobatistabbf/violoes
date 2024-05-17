from abc import ABCMeta, abstractmethod
import copy
from prototype import  violao


class violao_classico(violao):
    def __init__(self):
        self.material = "Madeira"
        self.numero_cordas = "6"
        self.nivel = "Iniciante"

    def tocar(self):
        pass

    def afinar(self):
        pass


class violao_folk(violao):
    def __init__(self):
        self.material = "Madeira"
        self.numero_cordas = "6"
        self.nivel = "Intermediario"

    def tocar(self):
        pass

    def afinar(self):
        pass

class violao_flet(violao):
    def __init__(self):
        self.material = "Madeira Fina"
        self.numero_cordas = "6"
        self.nivel = "Profissional"

    def tocar(self):
        pass

    def afinar(self):
        pass

class violao_jumbo(violao):
    def __init__(self):
        self.material = "Madeira(Arredondado)"
        self.nivel = "Profissional"
        self.numero_cordas = "6"

    def tocar(self):
        pass

    def afinar(self):
        pass

class violao_7_cordas(violao):
    def __init__(self):
        self.material = "Madeira"
        self.numero_cordas = "7"
        self.nivel = "Profissional"

    def tocar(self):
        pass

    def afinar(self):
        pass

class violao_12_cordas(violao):
    def __init__(self):
        self.material = "Madeira";
        self.numero_cordas = "12"
        self.nivel = "Profissional"

    def tocar(self):
        pass

    def afinar(self):
        pass

class violao_zero(violao):
    def __init__(self):
        self.material = "Madeira"
        self.numero_cordas = "6"
        self.nivel = "Intermediario"

    def tocar(self):
        pass

    def afinar(self):
        pass


class violao_duplo_zero(violao):
    def __init__(self):
        self.material = "Madeira"
        self.numero_cordas = "6"
        self.nivel = "Intermediario"

    def tocar(self):
        pass

    def afinar(self):
        pass


class violao_triplo_zero(violao):
    def __init__(self):
        self.material = "Madeira"
        self.numero_cordas = "6"
        self.nivel = "Intermediario"

    def tocar(self):
        pass

    def afinar(self):
        pass












