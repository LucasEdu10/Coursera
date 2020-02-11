num = int(input('Digite um numero inteiro: '))

indo = True
i = 1
total = 0

while i <= num:
	if num % i == 0:
		total += 1
	i += 1

if total == 2:
	print('primo')
else:
	print('não primo')

# Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo.
# Se o número for primo, imprima "primo".
# Caso contrário, imprima "não primo". 