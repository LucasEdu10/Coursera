# Escreva a função fizzbuzz que recebe como parâmetro um número inteiro e devolve

# 'Fizz' se o número for divisível por 3 e não for divisível por 5;

# 'Buzz' se o número for divisível por 5 e não for divisível por 3;

# 'FizzBuzz' se o número for divisível por 3 e por 5;

# Caso o número não seja divisível 3 e também não seja divisível por 5, ela deve devolver o número recebido como parâmetro.

x = int(input('Digite um numero: '))

def fizzBuzz(x):
	if ((x % 3) == 0) and ((x % 5) == 0):
		print('FizzBuzz')
	
	elif (x % 3) == 0:
		if (x % 5) != 0:
			print('Fizz')
	elif (x % 5) == 0:
		if (x % 3) !=0:
			print('Buzz')
	else:
		print(x)

fizzBuzz(x)