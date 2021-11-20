salario = float(input("Informe o salário: "))

aumento = int(input("Informe a porcentagem de aumento: "))
resultado = salario + (salario * aumento / 100)

print("O salário antigo era de: ", salario)
print("O salário após o aumento foi de: ", resultado)