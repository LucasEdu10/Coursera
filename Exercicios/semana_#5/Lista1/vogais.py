
#letra = input('Digite uma vogal: ')
vogais = ['a','e','i','o','u']

def vogal(letra):
	if letra.lower() in vogais:
		return True
	else:
		return False

# Escreva a função vogal que recebe um único caractere como parâmetro
# e devolve True se ele for uma vogal e False se for uma consoante.