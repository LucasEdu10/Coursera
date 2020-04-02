## JOGO NIM ##

jogada = 0

def partida():
	print("Bem vindo ao JOGO NIM!")
	print("")
	print("ESCOLHA O MODO DE JOGO: ")
	print("[1] - Partida ISOLADA")
	print("[2] - Partida como CAMPEONATO")
	print("")


	#solicita o modo é quantidade de peças/jogadas
	modo = int(input("Digite o modo: "))

	# indicadores de passagem 
	passouU = True
	passouPC = False

	#VERIFICA O MODO DO JOGO
	if modo == 1:
		print('================= MODO ISOLADA =================')
		print('')
		n = int(input('Quantidade de peças!?: '))
		m = int(input('Quantidade de peças por jogada!?: '))
		print('')
		while(n > 0):
			
			# Verifica se o numero é multiplo de m+1
			if n % (m + 1) == 0:
				# Indicador de passagem, para a mensagem de começar
				if passouU == True:
					passouU = False
					print('#### Pode começar senhor(a) ####')
					jogada = usuario_escolhe_jogada(n,m)
				else:
					jogada = usuario_escolhe_jogada(n,m)
			else:
				if passouU == True:
					print('#### Computador Começa ####')
					passouPC = True
					if passouPC == True:
						jogada = computador_escolhe_jogada(n,m)
				else:
					passouPC = True
					if passouPC == True:
						jogada = computador_escolhe_jogada(n,m)
				
			# Diminui o numero das peças
			n = n - jogada
			print('')
			print('Restam apenas {} peças em jogo.\n'.format(n))

		# Mostra quem ganhou a partida solo
		if n == 1:
			print('Você ganhou!!')
			return 1
		else:
			print("O computador ganhou!!")
			return 0		
	else:
		print('============== MODO CAMPEONATO ==============')
		print('')

def computador_escolhe_jogada(n,m):
	print('')
	print('Vez do computador!!')

	if n <= m:
		# Retira todas as peças e ganha o jogo:
		return n

	else:
		# Verifica se é possível deixar uma quantia múltipla de m+1:
		quantia = n % (m+1)

		if quantia > 0:
			return quantia

		# Não é, então tire m peças:
		return m


def usuario_escolhe_jogada(n,m):
	print('')
	print('Sua vez!!')

	# Solicita ao usuário quantas peças irá tirar:
	jogada = int(input('Quantas peças irá tirar?: '))

	# Verifica se a jogada é valida
	if jogada > m or jogada <= 0:
		print('Numero invalido!! Digite de 1 a {}'.format(m))
		jogada = int(input('Informe o numero novamente: '))

	return jogada		

partida()
