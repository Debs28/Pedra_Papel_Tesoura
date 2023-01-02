import random

def jogar():
    opc = ['Pedra', 'Papel', 'Tesoura']
    print("====== PEDRA, PAPEL E TESOURA ======")
    escolha_jogador = input("Faça sua jogada:")
    computador = random.choice(opc)

    if escolha_jogador == computador:
        print(f'A escolha do jogador é: {escolha_jogador}')
        print(f'A escolha do computador é: {computador}')
        print("Empate! Jogar Novamente")

    elif escolha_jogador == opc[0] and computador == opc[1]:
        print(f'A escolha do jogador é: {escolha_jogador}')
        print(f'A escolha do computador é: {computador}')
        print("Computador Venceu!")

    elif escolha_jogador == opc[1] and computador == opc[2]:
        print(f'A escolha do jogador é: {escolha_jogador}')
        print(f'A escolha do computador é: {computador}')
        print("Computador Venceu!")

    elif escolha_jogador == opc[2] and computador == opc[0]:
        print(f'A escolha do jogador é: {escolha_jogador}')
        print(f'A escolha do computador é: {computador}')
        print("Computador Venceu!")

    else:
        print(f'A escolha do jogador é: {escolha_jogador}')
        print(f'A escolha do computador é: {computador}')
        print('Jogador Venceu!')
jogar()