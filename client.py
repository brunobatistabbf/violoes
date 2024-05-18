from cache import violoes_cache

def menu():
    print()
    print("Escolha um violão:")
    print("1. Violão Clássico")
    print("2. Violão Folk")
    print("3. Violão Flet")
    print("4. Violão Jumbo")
    print("5. Violão 7 Cordas")
    print("6. Violão 12 Cordas")
    print("7. Violão Zero")
    print("8. Violão Duplo Zero")
    print("9. Violão Triplo Zero")
    print()

if __name__ == '__main__':
    violoes_cache.load()

    while True:
        menu()
        escolha = input("Digite o numero do violão desejado ou SAIR para finalizar: ")

        if escolha.lower() == 'sair':
            break

        violao = violoes_cache.get_violao(escolha)
        if violao:
            print()
            print(f"Você escolheu: {violao.get_type()}")
            violao.tocar()
            violao.afinar()
        else:
            print("Violão não encontrado")
