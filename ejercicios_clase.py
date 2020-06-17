#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import csv
import re


def contar_lineas(archivo):
    '''Función para el calculo de lineas de un archivo ingresado
    por el usuario retornando la cantidad de lineas leidas.'''

    fi = open(archivo, 'r')
    cant_lineas = 0
    for line in fi: 
        cant_lineas += 1
        print(line)
    
    print("la cantidad de lineas leidas son:", cant_lineas)
    return cant_lineas
    fi.close()


def ej1():
    # Ejercicios con archivos txt
    cantidad_lineas = 0

    '''
    Realizar un prorgrama que cuenta la cantidad de líneas
    de un archivo. Abra el archivo "notas.txt" en modo "lectura",
    lea linea alinea el archivo, y cuente la cantidad de líneas.
    Al finalizar el proceso, imprimir en pantalla la cantidad
    de líneas leaidas.

    Como práctica de funciones, puede realizar la función
    "contar_lineas" que reciba como parámetro el nombre del archivo
    y cumpla el objetivo especificado, retornando la cantidad
    de líneas encontradas.
    '''
    archivo = input('Ingrese el nombre del archivo:\n')
    contar_lineas(archivo)
    

def ej2():
    # Ejercicios con archivos txt      # Solo copia las lineas pares :(
    cantidad_lineas = 0
    '''
    Copy paste!!
    Deberá abrir dos archivo txt, uno para lectura (fi) y otro
    para escritura (fo) (un archivo nuevo).
    El archivo abierto para lectura (fi) debe ser el archivo
    "notas.txt"

    Debe leer "línea por línea" el archivo "nota.txt" y copiar
    "línea a línea" en el archivo para escritura.

    A su vez, mientras va escribiendo "línea a línea" debe
    contar la cantidad de línea que se copiaron e imprimir
    al final del proceso el valor.
    '''

    # fi = open('notas.txt', 'r')
    # fo = open(.......)
    fi = open('notas.txt', 'r')
    fo = open('notas_1.txt', 'w')
        
    for line in fi:
        line = fi.readline()
        print(line)
        fo.write(line)
        cantidad_lineas += 1
    
    print('La cantidad de lineas copiadas son:', cantidad_lineas)
        
    # Recuerde cerrar los archivos al final ;)
    
    fi.close()
    fo.close()


def ej3():
    # Ejercicios con archivos CSV
    archivo = 'propiedades.csv'
    '''
    Realice un programa que abra el archivo CSV "propiedades.csv"
    en modo lectura. Recorrar dicho archivo y contar
    la cantidad de departamentos de 2 ambientes y la cantidad
    de departamentos de 3 ambientes disponibles.
    Al finalizar el proceso, imprima en pantalla los resultados.
    '''
    with open('propiedades.csv') as csvfile:
        datos = list(csv.DictReader(csvfile))
        conteo_2 = 0
        conteo_3 = 0

        for i in range(len(datos)):
            if datos[i].get('ambientes') == '2':
                conteo_2 += 1
                print(datos[i])
            if datos[i].get('ambientes') == '3':
                conteo_3 += 1
                print(datos[i])
        print('La cantidad de departamentos de 2 ambientes son', conteo_2)
        print('La cantidad de departamentos de 2 ambientes son', conteo_3)

def ej4():
    # Ejercicios con diccionarios
    # inventario = {'manzanas': 6}

    '''
    Realice un programa que pida por consola
    el nombre de una fruta o verdura y luego
    pida la cantidad que hay en stock
    Agregar al diccionario el par:
    <fruta>:<cantidad>
    Esta operacion se debe realizar en un bucle
    hasta ingresar como fruta/verdura la palabra "FIN"

    Al finalizar el bucle anterior, debe generar otro bucle
    en donde se pida ingresar la fruta o verdura que desea
    conocer su estado de stock.
    Deberá imprimir en pantalla la cantidad de esa fruta en
    inventario, y en caso de no exista ese elemento en nuestro
    inventario se debe imprimir en pantalla "Elemento no encuentrado"
    NOTA: Proponemos utilizarel método "get" que devuelve "None" si el
    elemeto no existe en el diccionario.

    Se debe terminar ese segundo bucle cuando se ingrese la palabra FIN
    '''
    
    # 1) Bucle 1
    # Generar y completar el diccionario con las frutas y cantidades
    # ingresadas por consola hasta ingresar la palabra "FIN"
    inventario = {}
    frut_verd = True

    while True:
        frut_verd = input('Ingrese la fruta o verdura:\n')
        if frut_verd != 'FIN':
            cantidad = int(input('Ingrese la cantidad:\n'))
            inventario[frut_verd] = cantidad
        else:
            break
    
    print(inventario)

    # 2) Bucle 2
    # Ingresar por consola la fruta que desea conocer en stock
    # Finalizar cuando la fruta ingresada sea igual a "FIN"
    
    frut_verd = True
    while True:
        frut_verd = input('Ingrese la fruta o verdura a buscar\n')    
        if frut_verd != 'FIN':
            for k, v in inventario.items():
                if k == frut_verd:
                    print(inventario[frut_verd])
        else:
            break

def ej5():
    # Ejercicios con archivos CSV
    inventario = {}

    '''
    Basado en el ejercicio anterior, genere un archivo CSV
    (abrir un archivo CSV como escritura) que posea las siguientes
    columnas:
    1) 'Fruta Verdura'
    2) 'Cantidad'

    Estas dos columnas representan el nombre de las dos "claves"
    del diccionario que utilizaremos para escribir en el archivo CSV

    writer.writerow({'Fruta Verdura': ....., 'Cantidad': ....})

    Deberá realizar un bucle en donde en cada iteracion del bucle
    se le socilitará por consola que ingrese un tipo de fruta o verdura
    y su cantidad, deberá escribir una línea en el archivo CSV (una fila)
    con esa información ingresada.
    El bucle finalizará cuando se ingrese como fruta o verdura
    la palabra "FIN"

    Al finalizar deberá tener un archivo (con el nombre que usted haya
    elegido) con todas las filas completas en las dos columnas especificadas
    con todas las frutas o verduras ingresadas y sus cantidades
    '''
    # Recuerde crear el header correspondiente con "writeheader", el cual
    # se debe especificar al abrir el archivo.

    csvfile = open('ec5_verduleria.csv', 'w', newline='')

    header = ['Fruta Verdura', 'Cantidad']
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()

    # Bucle....

    while True:
        frut_verd = input('Ingrese la fruta o verdura:\n')
        if frut_verd != 'FIN':
            cantidad = int(input('Ingrese la cantidad:\n'))
            writer.writerow({'Fruta Verdura': frut_verd, 'Cantidad': cantidad})
        else:
            break

    # writer.writerow({'Fruta Verdura': ....., 'Cantidad': ....})

    csvfile.close()
    

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej5()
