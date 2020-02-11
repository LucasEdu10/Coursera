
num = int(input('Digite o valor de x: '))

def e_primo(x):
	if x >= 2:
		for y in range( 2, x ):
			if not ( x % y ):
				return False
	else:
		return False

	return True

def maior_primo(num):
	for n in range(num, 0, -1):
		if e_primo(n):
			print(n)
		break

'''
def ehPrimo(x):
    if x >= 2:
        for y in range( 2, x ):
            if not ( x % y ):
                return False
    else:
        return False

    return True

num = int(input("Entre com um numero: "))

for n in range( num, 0, -1 ):
    if ehPrimo(n) :
        print n
        break
'''






# Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2
# como parâmetro e devolve o maior número primo menor ou igual ao número passado à função