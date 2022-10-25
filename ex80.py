valores = []
for  indices in range(0, 5):
    v = (int(input('Digite o valor:')))
    if indices == 0:
        valores.append(v)
    elif v > len(valores)-1:
        valores.append(v)

print(valores)