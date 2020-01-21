dice = int(input('Por favor, entre com o número de segundos que seja converter: '))

day = dice // 86400
rest = dice % 86400

time = rest // 3600
rest = rest % 3600

minute = rest // 60
seconds = rest % 60

print(day,'dias,',time,'horas,',minute,'minutos e',seconds,'segundos')