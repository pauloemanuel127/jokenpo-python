import tkinter as tk
from tkinter import PhotoImage
import random
import interface_cases as ic

#definindo a janela (Aqui estão definidas a janela, cor de fundo, titulo,
#icone, posição e tamanho da janela)
root = tk.Tk()
root.title("Jokenpô")
root.config(bg="#00674f")

try:

    root.iconbitmap("icone_imagens/jokenpo_page_icon.ico")

except tk.TclError:
    
    try:

        icone = PhotoImage(file="icone_imagens/jokenpo_page_icon.png")
        root.iconphoto(False, icone)

    except Exception:

        pass

largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()

x = (largura_tela - 1200)//2
y = (altura_tela - 700)//2

root.geometry(f"1200x700+{x}+{y}")
root.resizable(False,False)

foto1 = PhotoImage(file="icone_imagens/image_2.png")
foto2 = PhotoImage(file="icone_imagens/image_1.png")

#Fazendo os labels e botões da pagina de entrada
def pagina_entrada():
    """
    Tela inicial do jogo,
    responsavel por levar para qualquer outra
    """
    #Fazendo os labels e botões da pagina de jogo
    #=================TELA DE JOGO=================

    def jogo():
        """
        Função que gera a tela de jogo 
        onde o usuario pode escolher entre 3 opções de jogadas
        """

        #=========================TELA DA JOGADA============================

        def jogada(jogada_player):
                """
                Função que cria a pagina final 
                e leva a variavel jogada player para a varificação de casos
                """

                def voltar():
                    """
                    Função responsavel por voltar a tela inicial na tela final
                    """

                    final.destroy()
                    back_button.destroy()
                    jogadas_text.destroy()
                    pagina_entrada()

                #==============================================================
                
                jogadas = ["rock", "papers", "scissors"]
                jogada_bot = random.choice(jogadas)

                resultado = ic.verificacao(jogada_player, jogada_bot)

                text.destroy()
                figura1.destroy()
                figura2.destroy()
                pedra_button.destroy()
                papel_button.destroy()
                tesoura_button.destroy()

                mensagem_completa = f"Você: {jogada_player} // Bot: {jogada_bot}"

                jogadas_text = tk.Label(
                     root,
                     text=mensagem_completa,
                     font=("Comic Sans MS", 30),
                     bg="#00674f",
                     fg="#fc4b08"
                )
                jogadas_text.place(relx=0.5, y=240, anchor="center")

                final = tk.Label(
                     root,
                     text=resultado,
                     font=("Comic Sans MS", 45),
                     bg="#00674f",
                     fg="#fc4b08"
                )
                final.place(relx=0.5, rely=0.5, anchor="center")

                back_button = tk.Button(
                root,
                text="BACK",
                font=("Comic Sans MS", 35),
                bg="#58d68d",
                fg="#fc4b08",
                width="8",
                command=voltar
                )
                back_button.pack()
                back_button.place(relx=0.5, y=550, anchor="center")

        #================================================================================


        game_title.destroy()
        game_subtitle.destroy()
        press_to_play.destroy()
        start_button.destroy()
        credits_button.destroy()
        exit_button.destroy()

        text = tk.Label(
            root,
            text="Choose an option:",
            font=("Comic Sans MS", 45),
            bg="#00674f",
            fg="#fc4b08"
        )
        text.pack()

        figura1 = tk.Label(
            root,
            image=foto1,
            bg="#00674f"
        )
        figura1.pack()
        figura1.place(x=110, y=220)

        figura2 = tk.Label(
            root,
            image=foto2,
            bg="#00674f"
        )
        figura2.pack()
        figura2.place(x=790, y=220)

        pedra_button = tk.Button(
            root,
            text="ROCK",
            font=("Comic Sans MS", 35),
            bg="#58d68d",
            fg="#fc4b08",
            width="10",
            command=lambda: jogada("rock")
        )
        pedra_button.pack()
        pedra_button.place(relx=0.5, y=200, anchor="center")

        papel_button = tk.Button(
            root,
            text="PAPERS",
            font=("Comic Sans MS", 35),
            bg="#58d68d",
            fg="#fc4b08",
            width="10",
            command=lambda: jogada("papers")
        )
        papel_button.pack()
        papel_button.place(relx=0.5, y=340, anchor="center")

        tesoura_button = tk.Button(
            root,
            text="SCISSORS",
            font=("Comic Sans MS", 35),
            bg="#58d68d",
            fg="#fc4b08",
            width="10",
            command=lambda: jogada("scissors")
        )
        tesoura_button.pack()
        tesoura_button.place(relx=0.5, y=480, anchor="center")

    #==============================================

    #Fazendo os labels e botões da pagina de creditos
    #=============TELA DE CREDITOS=============
    
    def creditos():
        """
        Função responsavel por gerar/levar para a tela de creditos
        """

        def voltar():
            """
            Função para voltar da tela de creditos para a tela original
            """

            credits.destroy()
            msg.destroy()
            back_button.destroy()
            pagina_entrada()

        #=================================================================

        game_title.destroy()
        game_subtitle.destroy()
        press_to_play.destroy()
        start_button.destroy()
        credits_button.destroy()
        exit_button.destroy()
        
        credits = tk.Label(
            root,
            text="CREDITS",
            font=("Comic Sans MS", 80, "bold"),
            bg="#00674f",
            fg="#fc4b08"
        )
        credits.pack()

        msg = tk.Label(
            root,
            text="Desenvolvido por:\nPaulo Emanuel\n(Github: pauloemanuel127)\n Imagens por:\n Geradas com IA",
            font=("Comic Sans MS", 30),
            bg="#00674f",
            fg="#fc4b08"
        )
        msg.pack()
        msg.place(relx=0.5, y=300, anchor="center")

        back_button = tk.Button(
            root,
            text="BACK",
            font=("Comic Sans MS", 35),
            bg="#58d68d",
            fg="#fc4b08",
            width="8",
            command=voltar
        )
        back_button.pack()
        back_button.place(relx=0.5, y=560, anchor="center")

    #===========================================

#====================TELA INICIAL====================

    game_title = tk.Label(
        root,
        text="Jokenpô",
        font=("Comic Sans MS", 80, "bold"),
        bg="#00674f",
        fg="#fc4b08"
    )
    game_title.pack()

    game_subtitle = tk.Label(
        root,
        text="The Game",
        font=("Comic Sans MS", 40),
        bg="#00674f",
        fg="#fc4b08"
    )
    game_subtitle.pack()

    press_to_play = tk.Label(
        root,
        text="PRESS START",
        font=("Comic Sans MS", 30),
        bg="#00674f",
        fg="#fc4b08"
    )
    press_to_play.pack(pady=10,side=tk.BOTTOM)

    start_button = tk.Button(
        root,
        text="START",
        font=("Comic Sans MS", 35),
        bg="#58d68d",
        fg="#fc4b08",
        width="8",
        command=jogo
    )
    start_button.pack()
    start_button.place(relx=0.5, y=300, anchor="center")

    credits_button = tk.Button(
        root,
        text="CREDITS",
        font=("Comic Sans MS", 35),
        bg="#58d68d",
        fg="#fc4b08",
        width="8",
        command=creditos
    )
    credits_button.pack()
    credits_button.place(relx=0.5, y=430, anchor="center")
    
    exit_button = tk.Button(
        root,
        text="EXIT",
        font=("Comic Sans MS", 35),
        bg="#58d68d",
        fg="#fc4b08",
        width="8",
        command=root.destroy
    )
    exit_button.pack()
    exit_button.place(relx=0.5, y=560, anchor="center")

#====================================================

pagina_entrada()
root.mainloop()
