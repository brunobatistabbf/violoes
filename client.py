from componentes.cache import violoes_cache

if __name__ == '__main__':
    violoes_cache.load()

    classico = violoes_cache.get_violao("1")
    print(classico.get_type())