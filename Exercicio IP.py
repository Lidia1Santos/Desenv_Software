texto = ('200.135.80.9 192.168.1.1 8.35.67.74 257.32.4.5 85.345.1.2 1.2.3.4 \
9.8.234.5 192.168.0.256')

temp  = open("tempp.txt","w")
for i in texto:
    temp.write(i)
lista = texto.split(' ')
print("IPs inseridos: ",lista)
temp.close()
campo = []
def valida_py(lista):
    for endereco in lista:
      
        if endereco < '255' :
            valido = []
            valido.append(endereco)
            print('IP Valido: ',valido)
                   
        else:
            invalido = []
            invalido.append(endereco)
            print ('IP Invalido:',invalido)  

valida_py(lista)

