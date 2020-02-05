num = int(input('Digite um numero inteiro: '))

indo = True
i = 1
total = 0
	
while i <= num and indo:
	if num % i == 0:
		total += 1
	i += 1

if total == 2:
	print('primo')
	indo = False
else:
	print('não primo')
	indo = False
