numero = int(input("Digite um numero:  "))
if  numero < 0 :
    n = numero * -1
    print(n)
elif numero > 10:
    numero2 = int(input("Digite outro numero:  "))
    n = numero - numero2
    print("A diferença é: ", n)
else:
    n = numero /5
    print(n)
print("Fim do programa")

