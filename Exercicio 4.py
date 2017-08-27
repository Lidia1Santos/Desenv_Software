arquivo = open("arquivo.txt","w")
for i in range(1):
    arquivo.write("Atividade 4 ")
arquivo.close()



arquivo = open("arquivo.txt","r")
for linha in arquivo:
    print("Texto: ",linha)
arquivo.close()



arquivo = open("arquivo.txt", "r")
copia = open("copia.txt", "w")
while 1:
    texto = arquivo.read(50)
    if texto == "":
        break
    copia.write(texto)
arquivo.close()
copia.close()



copia = open("copia.txt","r")
for linha in copia:
    print("Texto copiado: ",linha)
arquivo.close()


