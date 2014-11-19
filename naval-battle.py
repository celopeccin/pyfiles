""" Python 2.7.8 - Naval Battle """

from random import randint # Importamos de random o randint

board = [] # Definimos o tabuleiro

for i in range(0, 5): # Para cada i no range 0 a 5:
    i = ["O"] * 5 # Gera uma lista com 5 "O"
    board.append(i) # Adiciona esta lista ao tabuleiro deixando 5x5

def print_board(board): # Fun��o que imprime o tabuleiro
    for row in board: # Para cada linha do tabuleiro:
        print " ".join(row) # Imprima a linha separando-a por espa�o

def random_row(board): # Fun��o que retorna um numero de linha aleat�rio
    return randint(0, len(board) - 1)

def random_col(board): # Fun��o que retorna um numero de coluna aleat�rio
    return randint(0, len(board) - 1)

print "Play naval battle!"
print_board(board) # Chama a fun��o de impress�o do tabuleiro
ship_row = random_row(board) # Chama a fun��o da linha aleat�ria e guarda em uma vari�vel
ship_col = random_col(board) # Chama a fun��o da coluna aleat�ria e guarda em uma vari�vel

for turn in range(4): # O jogador tem 4 chances
    guess_row = int(raw_input("Guess Row: ")) # Pede para o jogador adivinhar a linha
    guess_col = int(raw_input("Guess Col: ")) # Pede para o jogador adivinhar a coluna

    if guess_row == ship_row and guess_col == ship_col: # Se estiver correta as posi��es informadas pelo jogador para o navio:
        print "Congratulations! You sank my battleship!" # Imprime que ele venceu
        break # Encerra o jogo
    else: # Se n�o:
        if guess_row not in range(5) or guess_col not in range(5): # Se o palpite n�o for dentro do oceano:
            print "Oops, that's not even in the ocean." # IMprime mensagem de erro
        elif board[guess_row][guess_col] == "X": # Se ele j� tentou aquela posi��o antes:
            print "Have you tried this position." # Imprime a informa��o que j� tentou antes
        else:
            print "You missed my battleship!"  # Imprmie que ele perdeu
            board[guess_row][guess_col] = "X"  # Atribui um X na posi��o indicada
            print_board(board) # Imprime o tabuleiro novamente com a posi��o atualizada
        if turn == 3: # Se o turno for o 3:
            print "Game Over!" # Imprime que o jogo acabou
        print "Turn: %s" %(turn + 1) # Imprime a rodada
