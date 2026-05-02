def pedra(jogada_player):
    jogada_player = jogada_player.lower()
    if jogada_player == 'papel':
         print('Você venceu!')
    elif jogada_player == 'tesoura':
         print('Você perdeu!')

def papel(jogada_player):
    jogada_player = jogada_player.lower()
    if jogada_player == 'tesoura':
         print('Você venceu!')
    elif jogada_player == 'pedra':
         print('Você perdeu!')

def tesoura(jogada_player):
    jogada_player = jogada_player.lower()
    if jogada_player == 'pedra':
        print('Você venceu!')
    elif jogada_player == 'papel':
         print('Você perdeu!')