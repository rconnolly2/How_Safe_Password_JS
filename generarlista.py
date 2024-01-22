lista_resultado = []
archivo = open("lista_passwords.txt", "r")
lineas = archivo.readlines()
for linea in lineas:
    
    lista_resultado.append(linea.replace("\n", ""))

print(lista_resultado)