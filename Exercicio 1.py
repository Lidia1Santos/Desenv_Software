def troca(numeros):
    cont = 0
    for x in numeros:
        if numeros[cont] > 0:
            numeros[cont] = 1
        else:
            numeros[cont] = 0
        cont = cont + 1
    print(numeros)



numeros = []
for i in range(30):
    numeros.append(int(input("Digite um numero: ")))
print(numeros)
troca(numeros)


