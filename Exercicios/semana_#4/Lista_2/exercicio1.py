num = int(input('Digite um numero inteiro: '))

indo = True

while indo:
	if num%2!=0:
		print('primo')
		indo = False
	else:
		print('não primo')
		indo = False
