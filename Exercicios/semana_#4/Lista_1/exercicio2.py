num = int(input('Digite um valor: '))
i = 0
p = 0
while i < num:
	p +=1
	if p % 2 != 0:
		print(p)
		p +=1
	i += 1