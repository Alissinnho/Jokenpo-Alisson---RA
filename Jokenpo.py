# Importando a biblioteca random para gerar as jogadas do computador
import random

placarJogador = 0
placarComputador = 0

# um loop while para comparar as jogadas
# LEGENDA: pedra = 1, papel = 2, tesoura = 3
while True:
    # o loop começa pedindo a jogada do usuario e depois realizando o sorteio da jogada do computador
    jogada = input("jogador faça sua jogada: ").lower()
    jogadaComputador = random.randint(1, 3)

    # agora começa as comparações entre as jogadas para ver quem venceu ou se deu empate
    # após a vericação é possivel 4 possibilidades:
    # o jogador ganhar, fazendo assim a soma de um ao placar pra ele
    # o Computador ganhar, fazendo a soma para o placar dele
    # empate, nesse caso os dois placares são somados a 1
    # ou uma jogada invalida pelo jogador, caso ele insira algo diferente de pedra, papel ou tesoura.
    # No caso de jogada invalida o programa é encerrado.
    if jogada == "pedra" and jogadaComputador == 3:
        placarJogador += 1
        print(f"Jogador venceu, placar: Jogador {placarJogador} x Computador {placarComputador}")
    elif jogada == "pedra" and jogadaComputador == 2:
        placarComputador += 1
        print(f"Computador venceu, placar: Jogador {placarJogador} x Computador {placarComputador}")
    elif jogada == "pedra" and jogadaComputador == 1:
        placarComputador += 1
        placarJogador += 1
        print(f"Empate, placar: Jogador {placarJogador} x Computador {placarComputador}")
    elif jogada == "papel" and jogadaComputador == 1:
        placarJogador += 1
        print(f"Jogador venceu, placar: Jogador {placarJogador} x Computador {placarComputador}")
    elif jogada == "papel" and jogadaComputador == 2:
        placarComputador += 1
        placarJogador += 1
        print(f"Empate, placar: Jogador {placarJogador} x Computador {placarComputador}")
    elif jogada == "papel" and jogadaComputador == 3:
        placarComputador += 1
        print(f"Computador venceu, placar: Jogador {placarJogador} x Computador {placarComputador}")
    elif jogada == "tesoura" and jogadaComputador == 1:
        placarComputador += 1
        print(f"Computador venceu, placar: Jogador {placarJogador} x Computador {placarComputador}")
    elif jogada == "tesoura" and jogadaComputador == 2:
        placarJogador += 1
        print(f"Jogador venceu, placar: Jogador {placarJogador} x Computador {placarComputador}")
    elif jogada == "tesoura" and jogadaComputador == 3:
        placarComputador += 1
        placarJogador += 1
        print(f"Empate, placar: Jogador {placarJogador} x Computador {placarComputador}")
    else:
        print("insira uma jogada válida")
        break

    # Apos a Comparação entre as duas jogadas, é perguntado ao usuario se ele deseja continuar
    # se o jogador digitar "não" o programa será encerrado e será imprimido os agradecimentos e o placar final.
    continua = input("Deseja continuar jogando? sim ou não ").lower()
    if continua == "Não" or continua == "não":
        print("Obrigado por jogar! o Alisson agradece :) ")
        print()
        print(f"Placar final: Jogador {placarJogador} x Computador {placarComputador}")
        break