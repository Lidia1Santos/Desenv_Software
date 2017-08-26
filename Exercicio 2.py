def troca(numeros):
    cont = 0
    for x in numeros:
        if numeros[cont] < 0:
            numeros[cont] = 0
        elif numeros[cont]>= 0 and numeros[cont]<=10:
            numeros[cont] = 1
        else:
            numeros[cont] = 2
        cont = cont + 1
    print(numeros)



numeros = []
for i in range(4):
    numeros.append(int(input("Digite um numero: ")))
print(numeros)
troca(numeros)

