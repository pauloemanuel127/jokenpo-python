#Projeto simples de um jogo de jokenpo

import random
import cases as c

while True:
    jogada_player = input("Escolha sua jogada: pedra, papel, tesoura. Digite exit para sair.\n" )
    jogadas_bot = ['pedra', 'papel', 'tesoura']
    jogada_bot = random.choice(jogadas_bot)

    if jogada_player.lower() == 'exit':
        print('Obrigado por jogar!')
        break
    
    elif jogada_bot == jogada_player.lower():
        print('Empate')

    elif jogada_bot == 'pedra':
        c.pedra(jogada_player)

    elif jogada_bot == 'papel':
        c.papel(jogada_player)

    elif jogada_bot == 'tesoura':
        c.tesoura(jogada_player)