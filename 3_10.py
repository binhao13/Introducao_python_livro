s = float(input("Digite seu salário: "))
a = float(input("Digite a porcentagem de aumento: "))
n = s*(1+a/100)
au = s*(a/100)
print(f"Seu aumento foi de R${au:.2f}")
print(f"Seu novo salário é R${n:.2f}")