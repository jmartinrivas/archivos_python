# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv


def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    stock_tornillos = 0
    try:
        archivo_stock = open("stock.csv","r")
    except:
        print("no existe el archivo al que intenta acceder, por favor verifique")

    stock_total = list(csv.DictReader(archivo_stock))
    for productos in stock_total:
        for k, v in productos.items():
            if k == "tornillos":
                stock_tornillos += int(v)
    print("El stock de tornillos total es:",stock_tornillos)

    archivo_stock.close()



def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    try:
        with open("propiedades.csv","r") as archivo_propiedades:
            base_propiedades = list(csv.DictReader(archivo_propiedades))
    except:
        print( "No existe el archivo al que intenta acceder, por favor verifique")
    
    contar_2amb = 0
    contar_3amb = 0
    for datos in base_propiedades:
        for k, v in datos.items():
            if k == "ambientes":
                try:
                    v = int(v)
                    if v == 2:
                        contar_2amb = contar_2amb + 1
                    elif v == 3:
                        contar_3amb = contar_3amb + 1
                except:
                    print("Valor invalido ({}) en fila {}".format(datos.get("ambientes"), datos.get("")))
    print("La cantidad de depto de 2 amb es:", contar_2amb)
    print("La cantidad de depto de 3 amb es:", contar_3amb)



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
