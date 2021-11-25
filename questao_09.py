dias = int(input("Informe a quantidade de dias: "))
horas = int(input("Informe a quantidade de horas: "))
minutos = int(input("Informe a quantidade de minutos: "))
segundos = int(input("Informe a quantidade de segundos: "))

totalSegundos = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos
print("O total de segundos é: ", totalSegundos)
