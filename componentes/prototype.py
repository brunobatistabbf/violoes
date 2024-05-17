from abc import ABCMeta, abstractmethod
import copy

class violao(metaclass= ABCMeta):

    def __init__(self):
        self.material = None
        self.numero_cordas = None
        self.nivel = None

    @abstractmethod
    def tocar(self):
        pass

    @abstractmethod
    def afinar(self):
        pass

    