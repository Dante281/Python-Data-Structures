fname = input("Enter file name: ")
fh = open(fname)

#Test line
#fh = open('romeo.txt')

#creamos la lista
lst = list()
    #añadimos el texto del fichero a line
for line in fh:
        # quitamos los espacios finales
    line = line.rstrip()
        #dividimos las palabras
    words = line.split()
        #Hacemos un nuevo loop para añadir las palabras a la lista sino existen ya.
    for z in words:
        if z in lst:
            continue
        else :
            lst.append(z)

    #ordenamos la lista
    lst.sort()
    #imprimimos la lista
print(lst)
