#Modulo responsavel pela verificação das possibilidades de resultados para o jogo de acordo com as jogadas
#Usa a jogada do bot como base, para verificar o caso de acordo com a jogada do player

def verificacao(jogada_player, jogada_bot):
    if jogada_player == jogada_bot:
        resultado = "Its a Tie"
        return resultado
    
    elif jogada_bot == "rock":
        if jogada_player == "papers":
            resultado = "Congratulations, You Win! :)"
            return resultado
        else:
            resultado = "To bad, You lose :("
            return resultado
        
    elif jogada_bot == "papers":
        if jogada_player == "scissors":
            resultado = "Congratulations, You Win! :)"
            return resultado
        else:
            resultado = "To bad, You lose :("
            return resultado
    
    elif jogada_bot == "scissors":
        if jogada_player == "rock":
            resultado = "Congratulation, You Win! :)"
            return resultado
        else:
            resultado = "To bad, You lose :("
            return resultado
