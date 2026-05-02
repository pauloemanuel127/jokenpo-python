# Jokenpô (Pedra, Papel e Tesoura) ✊✋✌️

Um projeto clássico de Jokenpô (Pedra, Papel e Tesoura) desenvolvido em Python. O objetivo deste projeto é aplicar lógicas de programação e estudar a criação de interfaces gráficas (GUI) utilizando a biblioteca **Tkinter**.

> ⚠️ **Status do Projeto:** A interface gráfica está atualmente em desenvolvimento. No entanto, o jogo base já é **100% funcional e jogável através do terminal**!

## 🎮 Funcionalidades

- **Jogo via Terminal:** Jogue contra um "bot" (computador) com escolhas aleatórias. O sistema reconhece vitórias, derrotas e empates.
- **Lógica Modular:** As regras de vitória e derrota estão separadas em um arquivo específico (`cases.py`), mantendo o código principal limpo e organizado.
- **Interface Gráfica (Em construção):** Um menu principal feito com Tkinter, contando com botões estilizados, página de créditos e artes em *pixel art* com tema de anime (Gon e Killua).

## 📁 Estrutura dos Arquivos

- `jokenpo_game.py`: O arquivo principal para rodar o jogo pelo terminal.
- `cases.py`: Módulo que contém a lógica de verificação das regras do jogo (quem ganha de quem).
- `interface.py`: Arquivo de desenvolvimento da interface gráfica do usuário (GUI) com Tkinter.
- `image_1.png` / `image_2.png`: Sprites em pixel art utilizados na interface.
- `jokenpo_page_icon.ico`: Ícone da janela do aplicativo.

## 🚀 Como Jogar

Certifique-se de ter o [Python](https://www.python.org/) instalado na sua máquina.

**Para jogar pelo Terminal (Versão Completa):**
1. Abra o seu terminal na pasta do projeto.
2. Execute o comando:
   ```bash
   python jokenpo_game.py
   ```
3. Digite sua jogada (`pedra`, `papel` ou `tesoura`) e veja o resultado. Para sair, digite `exit`.

**Para visualizar a Interface Gráfica (Em desenvolvimento):**
1. Abra o seu terminal na pasta do projeto.
2. Execute o comando:
   ```bash
   python interface.py
   ```
3. Navegue pelo menu criado com Tkinter.

## 👨‍💻 Desenvolvedor

- **Paulo Emanuel** - [GitHub: @pauloemanuel127](https://github.com/pauloemanuel127)

*Nota: As artes em pixel art utilizadas na interface gráfica foram geradas por Inteligência Artificial.*
