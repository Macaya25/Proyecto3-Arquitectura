try:
    file = open("instrucciones.txt", 'r')
except IOError:
    print("No se encontro el archivo")
    exit()


Lineas = file.readlines()
for linea in Lineas:
    print(linea.split())
file.close()
