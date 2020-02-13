# Escreva a função fizzbuzz que recebe como parâmetro um número inteiro e devolve

# 'Fizz' se o número for divisível por 3 e não for divisível por 5;

# 'Buzz' se o número for divisível por 5 e não for divisível por 3;

# 'FizzBuzz' se o número for divisível por 3 e por 5;

# Caso o número não seja divisível 3 e também não seja divisível por 5, ela deve devolver o número recebido como parâmetro.

#x = int(input('Digite um numero: '))

FizzBuzz = 'FizzBuzz'
Fizz = 'Fizz'
Buzz = 'Buzz'

def fizzbuzz(x):
	if ((x % 3) == 0) and ((x % 5) == 0):
		return FizzBuzz
	
	elif (x % 3) == 0:
		if (x % 5) != 0:
			return Fizz
	elif (x % 5) == 0:
		if (x % 3) !=0:
			return Buzz
	else:
		return x

#fizzBuzz(x)