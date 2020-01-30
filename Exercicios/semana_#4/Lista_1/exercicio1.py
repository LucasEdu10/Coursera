# n = int(input("Digite o valor de n: "))
# fat = 1
# i = 2
# while i <= n:
# 	fat = fat*i
# 	i = i + 1
# 	print("O valor de %d! eh =" %n, fat)

n = int(input('Digite um valor para soma: '))

def soma(n):
	if n == 0:
		return 0
	else:
		return soma(n-1) + n
print(soma(n))



def fatorial(n):
	if n == 0:
		return 1
	else:
		return fatorial(n-1) * n
print(fatorial(n))