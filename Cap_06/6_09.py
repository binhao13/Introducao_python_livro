l = [15,7,27,39]
p = int(input("Digite o valor a procurar: "))
v = int(input("Digite outro valor a procurar: "))
x = 0
y = 100
z = 100
achou1 = False
achou2 = False
while x < len(l):
    if l[x] == p:
        print(f"p:{p} encontrado")
        achou1 = True
        y = x
    elif l[x] == v:
        print(f"v:{v} encontrado")
        achou2 = True
        z = x
    elif achou1 and achou2:
        break
    x += 1
if achou1 == False:
    print(f"p: {p} não encontrado")
elif achou2 == False:
    print(f"v: {v} não encontrado")
if y < z and achou1:
    print(f"p foi achado primeiro")
elif achou2:
    print(f"v foi achado primeiro")