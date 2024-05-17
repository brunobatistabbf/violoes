from abc import ABCMeta, abstractmethod
import copy
from prototype import violao
from violoes import violao_classico, violao_flet, violao_folk, violao_zero, violao_jumbo, violao_duplo_zero, violao_triplo_zero, violao_12_cordas, violao, violao_7_cordas

class violoes_cache:
    cache = {}

    @staticmethod
    def get_violao(sid):
        VIOLAO = violoes_cache.cache.get(sid, None)
        return  VIOLAO.clone()

    @staticmethod
    def load():
        classico = violao_classico()
        classico.set_id("1")
        violoes_cache.cache[classico.get_id()] = classico

        folk = violao_folk()
        folk.set_id("2")
        violoes_cache.cache[folk.get_id()] = folk

        flet = violao_flet()
        flet.set_id("3")
        violoes_cache.cache[flet.get_id()] = flet

        jumbo = violao_jumbo()
        jumbo.set_id("4")
        violoes_cache.cache[jumbo.get_id()] = jumbo

        cordas7 = violao_7_cordas()
        cordas7.set_id("5")
        violoes_cache.cache[cordas7.get_id()] = cordas7

        cordas12 = violao_12_cordas()
        cordas12.set_id("6")
        violoes_cache.cache[cordas12.get_id()] = cordas12

        zero = violao_zero()
        zero.set_id("7")
        violoes_cache.cache[zero.get_id()] = zero

        duplo_zero = violao_duplo_zero()
        duplo_zero.set_id("8")
        violoes_cache.cache[duplo_zero.get_id()] = duplo_zero

        triplo_zero = violao_triplo_zero()
        triplo_zero.set_id("9")
        violoes_cache.cache[triplo_zero.get_id()] = triplo_zero

