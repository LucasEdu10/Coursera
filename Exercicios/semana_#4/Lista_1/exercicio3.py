n = int(input('Digite um numero: '))

indo = True
result = 0

while indo:
	if n > 0:
		result += n % 10
		n = int(n/10)
	else:
		indo = False
print(result)


#Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída