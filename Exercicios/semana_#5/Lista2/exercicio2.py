# Reescreva a função 'maximo' do outro exercício,
# que devolve o maior valor dentre dois inteiros recebidos, 
# para que ela passe a receber 3 valores inteiros como parâmetros e devolva o maior dentre eles.

# Exemplos de execução no Python Shell

def maximo(x,y,z):

	if x > y:
		local = x
	else:
		local = y

	if local > z:
		return local
	else:
		return z

#maximo(x,y,z)		