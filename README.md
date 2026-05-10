# Jokenpô (Pedra, Papel e Tesoura) ✊✋✌️

Um projeto clássico de Jokenpô (Pedra, Papel e Tesoura) desenvolvido em Python. O objetivo deste projeto foi aplicar lógicas de programação, separação de responsabilidades (MVC) e criar uma interface gráfica (GUI) do zero utilizando a biblioteca **Tkinter**.

> 🎉 **Status do Projeto:** Concluído! O jogo possui tanto a versão clássica de terminal quanto uma Interface Gráfica 100% funcional.

## 🎮 Funcionalidades

- **Interface Gráfica Completa:** Menu principal, tela de jogo interativa com botões, cálculo de resultados em tempo real e tela de créditos.
- **Jogo via Terminal:** Uma versão alternativa para jogar diretamente pelo console contra o computador.
- **Arquitetura Limpa (Clean Code):** As lógicas de vitória, derrota e empate estão totalmente separadas da interface visual, facilitando a manutenção do código.
- **Artes Personalizadas:** Uso de *pixel art* com tema de anime (Gon e Killua) para ilustrar as escolhas na tela.

## 📁 Estrutura dos Arquivos

A organização do projeto foi pensada para separar recursos visuais de lógica de programação:

- `interface.py`: Arquivo principal da Interface Gráfica (GUI). É o executável que abre a janela do jogo.
- `interface_cases.py`: Módulo contendo a lógica e as regras do jogo exclusivas para alimentar a interface gráfica.
- `jokenpo_game.py`: O arquivo principal para rodar a versão clássica do jogo pelo terminal.
- `cases.py`: Módulo com a lógica de regras voltada para a versão de terminal.
- `icone_imagens/`: Pasta (Asset folder) que guarda todos os recursos visuais:
  - `image_1.png` / `image_2.png`: Sprites em pixel art utilizados na tela de combate.
  - `jokenpo_page_icon.ico`: Ícone oficial da janela do aplicativo.

## 🚀 Como Jogar

Certifique-se de ter o [Python](https://www.python.org/) instalado na sua máquina.

**Para jogar pela Interface Gráfica (Recomendado):**
1. Abra o seu terminal na pasta do projeto.
2. Execute o comando:
   ```bash
   python interface.py
   ```
3. Navegue pelo menu, clique em **START** e faça suas escolhas clicando nos botões!

**Para jogar pelo Terminal:**
1. Abra o seu terminal na pasta do projeto.
2. Execute o comando:
   ```bash
   python jokenpo_game.py
   ```
3. Digite sua jogada (`pedra`, `papel` ou `tesoura`) e veja o resultado. Para sair, digite `exit`.

## 👨‍💻 Desenvolvedor

- **Paulo Emanuel** - [GitHub: @pauloemanuel127](https://github.com/pauloemanuel127)

*Nota: As artes em pixel art utilizadas na interface gráfica foram geradas por Inteligência Artificial.*