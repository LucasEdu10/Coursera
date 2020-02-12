# Reescreva a função 'maximo' do outro exercício,
# que devolve o maior valor dentre dois inteiros recebidos, 
# para que ela passe a receber 3 valores inteiros como parâmetros e devolva o maior dentre eles.

# Exemplos de execução no Python Shell

x = int(input('DIGITE O X: '))
y = int(input('DIGITE O Y: '))
z = int(input('DIGITE O Z: '))

maior = x

def maximo(x,y,z):
	if y > maior:
		maior = y
	elif z > maior:
		maior = z

	print(maior)

#maximo(x,y,z)		