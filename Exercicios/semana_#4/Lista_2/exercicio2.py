num = int(input('Digite um numero inteiro: '))

indo = True

while indo:
	if num > 0:
		num = num % 10
		print(num)
		print('tem numeros iguais')
	else:
		indo = False
		print('não tem iguais')