# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+-----+
 |    |
      |
      |
      |
      |
=========''', '''

+-----+
 |    |
 O    |
      |
      |
      |
=========''', '''

+-----+
 |    |
 O    |
 |    |
      |
      |
=========''', '''

+-----+
 |    |
 O    |
/|    |
      |
      |
=========''', '''

+-----+
 |    |
 O    |
/|\   |
      |
      |
=========''', '''

+-----+
 |    |
 O    |
/|\   |
/     |
      |
=========''', '''

+-----+
 |    |
 X    |
/|\   |
/ \   |
      |
=========''']


# Função para remover acentos
import re
import unicodedata

def strip_accents(text):
    try:
        text = unicode(text, 'utf-8')
    except (TypeError, NameError): # unicode is a default on python 3 
        pass
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)

def text_to_id(text):
    text = strip_accents(text.lower())
    text = re.sub('[ ]+', '_', text)
    text = re.sub('[^0-9a-zA-Z_-]', '', text)
    return text

# Classe
class Hangman:

	# Método Construtor
	def __init__(self, word):
		self.word = word
		self.letra_errad = []
		self.letra_chute = []

	# Método para adivinhar a letra
	def guess(self, letter):
		if letter in text_to_id(self.word) and letter not in self.letra_chute:
			self.letra_chute.append(letter)
		elif letter not in text_to_id(self.word) and letter not in self.letra_errad:
			self.letra_errad.append(letter)
		else:
			return False
		return True

	# Método para verificar se o jogo terminou
	def hangman_over(self):
		return self.hangman_won() or (len(self.letra_errad) == 6)

	# Método para verificar se o jogador venceu
	def hangman_won(self):
		if '*' not in self.hide_word():
			return True
		return False

	# Método para não mostrar a letra no board
	def hide_word(self):
		carc = ''
		for letter in text_to_id(self.word):
			if letter not in self.letra_chute:
				carc += '*'
			else:
				carc += letter
		return carc

	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		print (board[len(self.letra_errad)])
		print ('\nPalavra: ' + self.hide_word())
		print ('\nLetras erradas: ',) 
		for letter in self.letra_errad:
			print (letter + ',', end='')
		print ()
		print ('\nLetras corretas: ',)
		for letter in self.letra_chute:
			print (letter + ',', end='')
		print ()

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word(difc):
	if difc == 1:
		with open("palavra_1.txt", "rt") as f:
			bank = f.readlines()
		return bank[random.randint(0, len(bank)-1)].strip()
	elif difc == 2:
		with open("palavra_2.txt", "rt") as f:
			bank = f.readlines()
		return bank[random.randint(0, len(bank)-1)].strip()
	elif difc == 3:
		with open("palavra_3.txt", "rt") as f:
			bank = f.readlines()
		return bank[random.randint(0, len(bank)-1)].strip()


# Função Main - Execução do Programa
def main():

	escolha = True
	while escolha:
		difc = int(input(" Escolha a dificuldade \n 1 - Fácil (palavra até 6 letras) "
						 "\n 2 - Médio (palavra até 8 letras) \n 3 - Difícil (palavra com mais de 8 letras) \n "
						 "0 - Para sair do jogo \n "))
		if difc == 1 or difc == 2 or difc == 3:
			escolha = False
		elif difc == 0:
			quit()
		else:
			print("\n Escolha inválida! \n Tente novamente \n\n")
	# Objeto
	game = Hangman(rand_word(difc))

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while not game.hangman_over():
		game.print_game_status()
		user_input = input('\n\nDigite uma letra: ')
		game.guess(user_input)

	# Verifica o status do jogo
	game.print_game_status()

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		print('\n\nParabéns! Você venceu!!')
	else:
		print('\n\nGame over! Você perdeu.')
		print('\nA palavra era *** ' + game.word + ' ***')

	print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
	main()
