from abc import ABCMeta, abstractmethod
import copy

class violao(metaclass= ABCMeta):

    def __init__(self):
        self.id = None
        self.material = None
        self.numero_cordas = None
        self.nivel = None

    @abstractmethod
    def tocar(self):
        pass

    @abstractmethod
    def afinar(self):
        pass

    @abstractmethod
    def clone(self):
        return copy.copy(self)

    @abstractmethod
    def set_id(self, sid):
        self.id = sid

    @abstractmethod
    def get_id(self):
        return  self.id

    @abstractmethod
    def get_type(self):
        return self.material