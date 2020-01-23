num_x1 = int(input('Digite o x do primeiro plano: '))
num_y1 = int(input('Digite o y do primeiro plano: '))
print('')
num_x2 = int(input('Digite o x do Segundo plano: '))
num_y2 = int(input('Digite o y do Segundo plano: '))


distance = ((num_x1 - num_x2) ** 2 + (num_y1 - num_y2)) ** 2

if distance >= 10:
	print('Longe')
else:
	print('Perto')
