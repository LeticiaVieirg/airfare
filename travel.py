# Função para criar um voo
def criar_voo(numero_do_voo, destino, capacidade):
    voo = {
        'numero_do_voo': numero_do_voo,
        'destino': destino,
        'capacidade': capacidade,
        'passageiros': []  # Começa com uma lista vazia de passageiros
    }
    return voo

# Função para verificar assentos disponíveis em um voo
def assentos_disponiveis(voo):
    return voo['capacidade'] - len(voo['passageiros'])

# Função para reservar um assento em um voo
def assentos_reservados(voo, nome_passageiro):
    if assentos_disponiveis(voo) > 0:
        voo['passageiros'].append(nome_passageiro)
        print(f"Assento reservado para {nome_passageiro} no voo {voo['numero_do_voo']}.")
    else:
        print(f"Não há assentos disponíveis no voo {voo['numero_do_voo']}.")

# Função para exibir os voo disponíveis
def voo_disponiveis(voo):
    print("Lista voo disponíveis:")
    for i, voo in enumerate(voo, start=1):
        print(f"{i}. Voo {voo['numero_do_voo']}: Destino - {voo['destino']}, Assentos disponíveis - {assentos_disponiveis(voo)}")


# Função principal
def main():
    # Lista de voo
    voo = [
        criar_voo("RJ765", "Rio de Janeiro", 5),
        criar_voo("BL923", "Brasilia", 5),
        criar_voo("NT489", "Natal", 5)
    ]

    #loop infinito
    while True:
        print("\n Seja bem-vindo ao Sistema de Reserva de Passagens Aéreas!")
        voo_disponiveis(voo)

        escolha = input("\nEscolha um voo (ou 's' para sair): ")

        # Sair do programa se o usuário escolher 's'
        if escolha.lower() == 's':
            break

        # Verificar escolha do usuário e reduzir uma passagem disponível
        if escolha == '1' and voo[0]['capacidade'] > 0:
            voo_selecionado = voo[0]
        elif escolha == '2' and voo[1]['capacidade'] > 0:
            voo_selecionado = voo[1]
        elif escolha == '3' and voo[2]['capacidade'] > 0:
            voo_selecionado = voo[2]
        else:
            print("Escolha inválida ou não há assentos disponíveis. Por favor, escolha novamente.")
    
        # Obter o nome do passageiro
        nome_passageiro = input("Digite seu nome: ")
        assentos_reservados(voo_selecionado, nome_passageiro)
        voo_selecionado['capacidade'] - 1

# Executar a função principal se o script estiver sendo executado diretamente
if __name__ == "__main__":
    main()
