try:
    file = open("Incorrecto.txt", 'r')
except IOError:
    print("No se encontro el archivo")
    exit()


Lineas = file.readlines()
instructions = ["CMP", "JEQ", "MOV", "SUB", "ADD", "JMP"]
for idx, linea in enumerate(Lineas):
    line = linea.split()
    if line[0] not in instructions:
        print("Error en la linea {}: {} \t{} no es una instruccion valida".format(idx+1, linea, line[0]))
    elif line[0][0] == "J":
        if "," in line[1]:
            print("Error en la linea {}: {} \tError de sintaxis, {} solo recibe un parametro.".format(idx+1, linea, line[0]))
    elif line[0] == "CMP":
        if line[1][0] != "#":
            try:
                float(line[1])
            except ValueError:
                print("Error en la linea {}: {} \tEl primer elemento no puede ser un literal".format(idx+1, linea, line[0]))
        else:
            print("Error en la linea {}: {} \tEl primer elemento no puede ser un literal".format(idx + 1, linea, line[0]))

    elif line[0] == "ADD":
        if line[1][0] == "(":
            print("Error en la linea {}: {} \tEl primer elemento no puede ser una direccion".format(idx + 1, linea, line[0]))

file.close()
