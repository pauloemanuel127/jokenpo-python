#Projeto simples de um jogo de jokenpo

import random
import cases as c

while True:

    #Armazena o input do jogador na variavel jogada_player, e escolhe um dos valores da lista jogadas_bot para ser o valor da jogada_bot
    jogada_player = input("Escolha sua jogada: pedra, papel, tesoura. Digite exit para sair.\n" )
    jogadas_bot = ['pedra', 'papel', 'tesoura']
    jogada_bot = random.choice(jogadas_bot)

    #Faz as verificações de qual caminho seguir, utilizando a jogada de bot como base para a verifcação nesse momento, 
    #E mandando a jogada do player como valor na função
    
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