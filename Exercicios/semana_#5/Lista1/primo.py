
#num = int(input('Digite o valor de x: '))

def ePrimo(x):
	if x >= 2:
		for y in range( 2, x ):
			if not ( x % y ):
				return False
	else:
		return False

	return True

def maior_primo(x):
	for n in range(x, 0, -1):
		if ePrimo(n):
			print(n)
			return n
#maior_primo(num)


# Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2
# como parâmetro e devolve o maior número primo menor ou igual ao número passado à função