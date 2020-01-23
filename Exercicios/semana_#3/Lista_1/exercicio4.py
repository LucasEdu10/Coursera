num = int(input('Digite um numero: '))


if num < 0:
	print(num,'Não é divisivel por 3 e 5')
elif (num % 3) == 0 or (num % 5) == 0:
		print('FizzBuzz')
else:
	print(num, 'Não é divisivel por 3 e 5')
