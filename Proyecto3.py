try:
    file = open("Incorrecto.txt", 'r')
except IOError:
    print("No se encontro el archivo")
    exit()


Lineas = file.readlines()
instructions = ["CMP", "JEQ", "MOV", "SUB", "ADD", "JMP"]
for linea in Lineas:
    line = linea.split()
    if line[0] not in instructions:
        print("Error en la linea: {} \t{} no es una instruccion valida".format(linea, line[0]))

file.close()
