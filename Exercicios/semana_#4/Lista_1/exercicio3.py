n = int(input('Digite um numero: '))

indo = True

while indo:
	if n % 10 != 0:
		result = n + n
		indo = False
		print(result)
	else:
		print(n)