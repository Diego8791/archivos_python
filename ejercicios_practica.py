#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"


import csv


def ej1():
    print("Cuenta caracteres")
    

    '''
    Realizar un prorgrama que cuenta la cantidad de caracteres
    (todo tipo de caracter, los espacios cuentan) de un archivo.
    Abra el archivo "text.txt" en modo "lectura", lea linea a
    linea el archivo, y cuente la cantidad de caracteres de cada línea.
    Debe realizar la sumatoria total de la cantidad de caracteres de todas
    las líneas para obtener el total del archivo e imprimirlo en pantalla
    '''
    # abrir el archivo texto.txt
    fi = open('texto.txt', 'r')
    
    cantidad_lineas = 0
    cantidad_letras = 0
  
    # Cuenta la cantidad de lineas en texto.txt
    for line in fi: 
        cantidad_lineas += 1
    print('La cantidad de lineas son', cantidad_lineas)

    # Vuelve el cursor al comienzo del texto
    fi.seek(0)

    # Cuenta la cantidad de caracteres en el texto
    for i in range(cantidad_lineas):    
        cantidad_letras += len(fi.readline())
    print('La cantidad de caracteres son', cantidad_letras)
    
    # cerrar el archivo texto.txt
    fi.close()


def ej2():
    print("Transcribir!")
    cantidad_letras = 0
    '''
    Deberá abrir un archivo txt para escritura (un archivo nuevo)
    Luego mediante un bucle deberá pedir por consola que
    se ingrese texto. Todo el texto ingresado por consola
    debe escribirse en el archivo txt, cada entrada de texto
    deberá ser una línea en el archivo.
    El programa termina cuando por consola no se ingresa
    nada (texto vacio). En ese momento se termina el bucle
    y se cierra el archivo.
    Durante la realización del bucle y el ingreso de texto por
    consola, se debe ir contanto cuandos caracteres se ingresaron
    por consola, al fin de al terminar el bucle saber cuantos
    caracteres se copiaron al archivo.
    NOTA: Recuerde agregar el salto de línea "\n" a cada entrada
    de texto de la consola antes de copiar la archivo.
    '''

    # Abrir el archivo eje_pract2.txt en modo write ('w')
    fo = open('eje_pract2.txt', 'w')

    line = ''
    total_caracteres = 0
        
    # bucle para introducir texto en archivo eje_pract2.txt
    while line != '\n':
        line = input('Ingrese linea de texto: \n')
        
        # acumulador de cantidad de caracteres ingresados por linea
        total_caracteres += len(line)
        
        # concatena '\n' para hacer el salto de linea
        line = line + '\n'
        
        # se copia a la memoria
        fo.writelines(line)
    
    print('Se han ingresado al texto', total_caracteres, 'caracteres')
                
    fo.close()

def ej3():
    print("Escrutinio de los alquileres de Capital Federal")
    cantidad_ambientes = 2

    '''
    Realizar un prorgrama que solicite la cantidad de
    ambientes de los alquileres que se desean analizar.
    Abra el archivo "propiedades.csv" y mediante un bucle analizar:
    1) Contar cuantos alquileres en "pesos" hay disponibles
    en la cantidad de ambientes deseados.
    2) Obtener el promedio del valor de los alquileres en "pesos"
    de la cantidad de ambientes deseados.
    3) Obtener el máximo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    4) Obtener el mínimo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    '''
    
    with open('propiedades.csv') as csvfile:
        data = list(csv.DictReader(csvfile))
       
        contador_ARS = 0
        acum_precios = 0
        list_precios = []

        for i in range(len(data)):
            if data[i].get('moneda') == 'ARS':
                contador_ARS += 1
                precio = float(data[i].get('precio'))
                list_precios.append(precio)
                # print(precio)
                acum_precios += precio
        
        promedio = acum_precios / contador_ARS
        print('La cantidad de alquileres en pesos son', contador_ARS)
        print('El promedio es', round(promedio, 2))
        print('El valor maximo es', max(list_precios))
        print('El valor minimo es', min(list_precios))
        

def ej4():
    print("Ahora sí! buena suerte :)")

    '''
    Para poder realizar este ejercicio deberán descargarse el
    dataset "2019 Ironman world championship results" del siguiente
    link:
    https://www.kaggle.com/andyesi/2019-ironman-world-championship-results/data#

    Una vez tengan descargado el archivo CSV lo pueden observar un poco.
    En principio le daremos importancia a las siguientes columnas:

    Division: Esta columna marca la divisón del corredor por experiencia o edad.
    Swim: Tiempo nadando
    Bike: Tiempo en bicicleta
    Run: Tiempo corriendo

    Queremos investigar las siguientes divisiones o categorias:
    - MPRO
    - M45-49
    - M25-29
    - M18-24

    De cada una de estas categorías de corredores deseamos que analices
    por separado el tiempo de Swim, Bike y Run. En cada caso (para los 3)
    se desea obtener
    1) El tiempo máximo realizado por un corredor en dicha categoria
    2) El tiempo mínimo realizado por un corredor en dicha categoria
    3) El tiempo promedio de dicha categoria

    Es decir, por ejemplo voy a investigar la categoria M45-49 en "Run"
    - Debo buscar de todos los M45-49 cual fue el mayor tiempo en Run
    - Debo buscar de todos los M45-49 cual fue el menor tiempo en Run
    - Debo buscar de todos los M45-49 el tiempo Run y calcular el promedio

    Para poder realizar este ejercicio necesitará muchas variables para almacenar
    los datos, puede organizarse como mejor prefiera, en listas, con diccionarios,
    lo que se sienta más comodo.

    Es valido recorrer todo el archivo para extrer la información ordenada
    y almacenarlas en listas según el criterio que escojan.

    NOTA:
    Recomendamos empezar de a poco, los primeros ensayos realizarlo
    con una sola categoría de edad en solo una sección (Bike, Run, Swim)
    de la carrera. Sería igual al ej4 la información recolectada y calculada.

    '''


if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    ej3()
    #ej4()
