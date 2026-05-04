import tkinter as tk
from tkinter import PhotoImage

#definindo a janela (Aqui estão definidas a janela, cor de fundo, titulo,
#icone, posição e tamanho da janela)
root = tk.Tk()
root.title("Jokenpô")
root.config(bg="#00674f")
root.iconbitmap("icone_imagens/jokenpo_page_icon.ico")

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

    #Fazendo os labels e botões da pagina de jogo
    #=================TELA DE JOGO=================

    def jogo():

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
            command=()
        )
        pedra_button.pack()
        pedra_button.place(x=450, y=140)

        papel_button = tk.Button(
            root,
            text="PAPER",
            font=("Comic Sans MS", 35),
            bg="#58d68d",
            fg="#fc4b08",
            width="10",
            command=()
        )
        papel_button.pack()
        papel_button.place(x=450, y=280)

        tesoura_button = tk.Button(
            root,
            text="SCISSORS",
            font=("Comic Sans MS", 35),
            bg="#58d68d",
            fg="#fc4b08",
            width="10",
            command=()
        )
        tesoura_button.pack()
        tesoura_button.place(x=450, y=420)

    #==============================================

    #Fazendo os labels e botões da pagina de creditos
    #=============TELA DE CREDITOS=============
    
    def creditos():
        
        #Função responsável por voltar para a tela principal
        #=============FUNÇÃO PARA VOLTAR=============

        def voltar():

            credits.destroy()
            msg.destroy()
            back_button.destroy()
            pagina_entrada()

        #============================================

    #=============TELA DE CREDITOS=============

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
        msg.place(x=350, y=200)

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
        back_button.place(x=480, y=550)

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
    start_button.place(x=480, y=250)

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
    credits_button.place(x=480, y=380)
    
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
    exit_button.place(x=480, y=510)

#====================================================

pagina_entrada()
root.mainloop()