#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Pedro Luis Lugo Garcia"
__email__ = "pllugo@gmail.com"
__version__ = "1.1"

# Variable global utilizada para el ejercicio de nota
notas = [70, 82, -1, 65, 55, 67, 87, 92, -1]

# Variable global utilizada para el ejercicio de temperaturas
temp_dataloger = [12.8, 18.6, 14.5, 20.8, 12.1, 21.2, 13.5, 18.6,
                  14.7, 19.6, 11.2, 18.4]


def ej1():
    print('Comenzamos a ponernos serios!')

    '''
    Realice un programa que pida por consola dos números que representen
    el principio y fin de una secuencia numérica.
    Realizar un bucle "for" que recorra esa secuencia armada con "range"
    y cuente cuantos números ingresados hay, y la sumatoria de todos los números
    Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    sino que va hasta el anterior
    '''

    # inicio = ....
    # fin = ....
    inicio = int(input('Ingrese el primero número de la secuencia\n'))
    fin = int(input('Ingrese el segundo número de la secuencia\n'))
    lista = list(range(inicio,fin+1)) #+ 1 para tomar todos los valores
    cantidad_numeros = 0
    sumatoria = 0

    for i in range(len(lista)):
        numero = lista[i]
        sumatoria = sumatoria + numero
        cantidad_numeros += 1
    print("Hay {} números".format(cantidad_numeros))
    print("La sumatoria es", sumatoria)
    promedio = sumatoria / cantidad_numeros
    print("El promedio es:", promedio)
    # cantidad_numeros ....
    # sumatoria ....

    # bucle.....

    # Al terminar el bucle calcular el promedio como:
    # promedio = sumatoria / cantidad_numeros

    # Imprimir resultado en pantalla

def verificar(numero): #Verificar si es un número el ingresado por consola
    try:
        float(numero)
        return True
    except:
        return False

def ej2():
    print("Mi Calculadora (^_^)")

    '''
    Tome el ejercicio de clase:
    <condicionales_python /  ejercicios_practica / ej3>,
    copielo a este ejercicio y modifíquelo, ahora se deberá ejecutar
    indefinidamente hasta que como operador se ingrese la palabra "FIN",
    en ese momento debe terminar el programa

    Se debe debe imprimir un cartel de error si el operador ingresado no es
    alguno de lo soportados o no es la palabra "FIN"
    '''
    
    # Realice una calculadora, se ingresará por línea de comando dos números
    # Luego se ingresará como tercera entrada al programa el símbolo de la operación
    # que se desea ejecutar
    # - Suma (+)
    # - Resta (-)
    # - Multiplicación (*)
    # - División (/)
    # - Exponente/Potencia (**)

    # Se debe efectuar el cálculo correcto según la operación ingresada por consola
    # Imprimir en pantalla la operación realizada y el resultado
    
  

    while True:
        numero_1 = input("Ingrese el primer número:\n")
        numero_2 = input("Ingrese el segundo número:\n")
        operacion = input(("""Ingrese la operación que desee realizar: 
        suma(+) 
        Resta(-) 
        Multiplicación(*) 
        División(/) 
        Exponente/Potencia (**)
        Por favor, indique: """))
        if verificar(numero_1) and verificar(numero_2): #verificar si los datos ingresados son validos
            print("Se han ingresado datos validos")
            primer_numero = float(numero_1)
            segundo_numero = float(numero_2)
            if operacion == "+":
                print("El resultado de la suma es:", primer_numero + segundo_numero)
            else:
                if operacion == "-":
                    print("El resultado de la resta es:", primer_numero - segundo_numero)
                else:
                    if operacion == "*":
                        print("El resultado de la multiplicación es:", primer_numero * segundo_numero)
                    else:
                        if operacion == "/":
                            print("El resultado de la división es:", primer_numero / segundo_numero)
                        else:
                            if operacion == "**":
                                print("El resultado del exponente/potencia es:", primer_numero ** segundo_numero)
                            else:
                                print("FIN")
                                break
            seguir_operacion = str(input("Ingrese un Si, si quiere seguir operando, un No para terminar:\n"))
            if seguir_operacion == "Si":
                continue
            else:
                print("FIN")
                break
        else:
            print("FIN")
            break
        
def calificacion(puntaje): #Funciín para la calificación según puntaje
    if puntaje >= 90:
        return "A"
    else:
        if puntaje >= 80:
            return "B"
        else:
            if puntaje >= 70:
                return "C"
            else:
                if puntaje >= 60:
                    return "D"
                else: 
                    return "F" #En éste punto ya el puntaje es menor a 60

def ej3():
    print("Mi organizador académico (#_#)")

    '''
    Tome el ejercicio de "calificaciones":
    <condicionales_python / ejercicios_clase / ej3>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento

    Las notas del estudinte se encuentran almacenadas en una
    lista llamada "notas" que ya hemos definido al comienzo del archivo

    Debe caluclar el promedio de todas las notas y luego transformar
    la califiación en una letra según la escala establecida en el ejercicio
    "calificaciones" <condicionales_python / ejercicios_clase / ej3>

    A medida que recorre las notas, no debe considerar como válidas aquellas
    que son negativas, en ese caso el alumno estuvo ausente

    Debe contar la cantidad de notas válidas y la cantidad de ausentes
    '''
    # Verifique la calificación de un estudiante según su
    # puntaje en un examen
    # puntaje = 70

    # Si el puntaje es mayor igual a 90 --> imprimir A
    # Si el puntaje es mayor igual a 80 --> imprimir B
    # Si el puntaje es mayor igual a 70 --> imprimir C
    # Si el puntaje es mayor igual a 60 --> imprimir D
    # Si el puntaje es menor a  60      --> imprimir F

    # Para calcular el promedio primero debe obtener la suma
    # de todas las notas, que irá almacenando en esta variable
    sumatoria = 0           # Ya le hemos inicializado en 0

    cantidad_notas = 0      # Aquí debe contar cuantas notas válidas encontró
    cantidad_ausentes = 0   # Aquí debe contar cuantos ausentes hubo

    # Realice aquí el bucle para recorrer todas las notas
    # y cacular la sumatoria
    for i in range(len(notas)):
        numero = notas[i]
        if numero >= 0:
            sumatoria = sumatoria + numero
            cantidad_notas += 1
            print("La calificación es :", calificacion(numero)) #llama a la función calificación e imprime
        else:
            cantidad_ausentes += 1
    # Terminado el bucle calcule el promedio como
    # promedio = sumatoria / cantidad_notas

    promedio = sumatoria / cantidad_notas
    print("El promedio es:", promedio)
    print("Hay {} de notas válidas".format(cantidad_notas))
    

    # Utilice la nota promedio calculada y transformela
    # a calificación con letras, imprima en pantalla el resultado
    print("El promedio", promedio, "transformado es:", calificacion(promedio))

    # Imprima en pantalla al cantidad de ausentes
    print("Hay {} ausentes".format(cantidad_ausentes))


def ej4():
    print("Mi primer pasito en data analytics")

    '''
    Tome el ejercicio:
    <condicionales_python / ejercicios_practica /ej5>,
    copielo a este ejercicio y modifíquelo para cumplir el
    siguiente requerimiento

    En este ejercicio se lo provee de una lista de temperatuas,
    esa lista de temperatuas corresponde a los valores de temperaturas
    tomados durante una temperorada del año en Buenos Aires.
    Ustede deberá analizar dicha lista para deducir
    en que temporada del año se realizó el muestreo de temperatura.
    La variable con la lista de temperaturas se llama "temp_dataloger"
    definida al comienzo del archivo

    Debe recorrer la lista "temp_dataloger" y obtener los siguientes
    resultados

    1 - Obtener la máxima temperatura
    2 - Obtener la mínima temperatura
    3 - Obtener el promedio de las temperatuas

    Los resultados se deberán almacenar en las siguientes variables
    que ya hemos preparado para usted.
    
    NOTA: No se debe ordenar la lista de temperaturas, se debe obtener
    el máximo y el mínimo utilizando los mismos métodos vistos
    durante la clase (ejemplos_clase)
    '''


    temperatura_max = None      # Aquí debe ir almacenando la temp máxima
    temperatura_min = None      # Aquí debe ir almacenando la temp mínima
    temperatura_sumatoria = 0   # Aquí debe ir almacenando la suma de todas las temp
    temperatura_promedio = 0    # Al finalizar el loop deberá aquí alamcenar el promedio
    temperatura_len = 0         # Aquí debe almacenar cuantas temperatuas hay en la lista

    # Colocar el bucle aqui......
    for i in range(len(temp_dataloger)):
        numero = temp_dataloger[i]
        temperatura_sumatoria = temperatura_sumatoria + numero
        temperatura_len += 1
        if (temperatura_max is None) or (numero > temperatura_max):
            temperatura_max = numero
        else:
            if (temperatura_min is None) or (numero < temperatura_min):
                temperatura_min = numero
    print("La temperatura {} es la máxima".format(temperatura_max))
    print("La temperatura {} es la mínima".format(temperatura_min))
    print("La cantidad de temperaturas son:", temperatura_len)
    temperatura_promedio = temperatura_sumatoria / temperatura_len
    print("El promedio de temperaturas es:", temperatura_promedio)
    # Al finalizar el bucle compare si el valor que usted calculó para
    # temperatura_max y temperatura_min coincide con el que podría calcular
    # usando la función "max" y la función "min" de python
    # función "max" --> https://www.w3schools.com/python/ref_func_max.asp
    # función "min" --> https://www.w3schools.com/python/ref_func_min.asp

    print("La máxima temperatura usando la función max es:", max(temp_dataloger))
    print("La mínima temperatura usando la función mmin es:", min(temp_dataloger))

    # Al finalizar el bucle debe calcular el promedio como:
    # temperatura_promedio = temperatura_sumatoria / cantidad_temperatuas

    # Corroboren los resultados de temperatura_sumatoria
    # usando la función "sum"
    # función "sum" --> https://www.w3schools.com/python/ref_func_sum.asp
    print("la sumatoria usando la función sum, es:", sum(temp_dataloger))

    '''
    Una vez que tengamos nuestros valores correctamente calculados debemos
    determinar en que epoca del año nos encontramos en Buenos Aires utilizando
    la estadística de años anteriores. Basados en el siguiente link realizamos
    las siguientes aproximaciones:

    verano -->      min = 19, max = 28
    otoño -->       min = 11, max = 20
    invierno -->    min = 8, max = 14
    primavera -->   min = 10, max = 24

    Referencia:
    https://es.weatherspark.com/y/28981/Clima-promedio-en-Buenos-Aires-Argentina-durante-todo-el-a%C3%B1o
    '''
    if (temperatura_min >= 19) and (temperatura_max <= 28):
        print("La estación es: Verano")
    else:
        if (temperatura_min >= 11) and (temperatura_max <= 20):
            print("La estación es: Otoño")
        else:
            if (temperatura_min >= 8) and (temperatura_max <= 14):
                print("La estación es: Invierno")
            else:
                if (temperatura_min >= 10) and (temperatura_max <= 24):
                    print("La estación es: Primavera")
    # En base a los rangos de temperatura de cada estación,
    # ¿En qué época del año nos encontramos?
    # Imprima el resultado en pantalla
    # Debe utilizar temperatura_max y temperatura_min para definirlo

def ordenar(listas): # Ordena una lista por orden alfabetico método de burbuja
    for i in range(len(listas)-1): # El range es hasta -1 porque voy a comparar con el de la derecha
        for j in range(len(listas)-1):
            if listas[j] > listas[j+1]:
                aux = listas[j]
                listas[j] = listas[j+1]
                listas[j+1] = aux
    return print("La palabra {} es la mayor por orden alfabetico".format(listas[0]))

def letras(lista_letras): #Ordena una lista por la cantidad de letras de las palabras
    for i in range(len(lista_letras)-1):
        for j in range(len(lista_letras)-1):
            if len(lista_letras[j]) > len(lista_letras[j+1]):
                aux = lista_letras[j]
                lista_letras[j] = lista_letras[j+1]
                lista_letras[j+1] = aux
    return print("La  palabra {} tiene la mayor cantidad de letras".format(lista_letras[len(lista_letras)-1]))

def ej5():
    print("Ahora sí! buena suerte :)")

    '''
    Tome el ejercicio:
    <condicionales_python / ejercicios_practica / ej4>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento

    Realize un programa que corra indefinidamente en un bucle, al comienzo de la
    iteración del bucle el programa consultará al usuario con el siguiente menú:
    1 - Obtener la palabra más grande por orden alfabético (usando el operador ">")
    2 - Obtener la palabra más grande por cantidad de letras (longitud de la palabra)
    3 - Salir del programa

    En caso de presionar "3" el programa debe terminar e informar por
    pantalla de que ha acabado,
    en caso contrario si se presionar "1" o "2" debe continuar con la siguiente tarea

    NOTA: Si se ingresa otro valor que no sea 1, 2 o 3 se debe enviar
    un mensaje de error y volver a comenzar el bucle
    (vea en el apunte "Bucles - Sentencias" para encontrar
    la sentencia que lo ayude a cumplir esa tarea)

    Si el bucle continua (se presionó "1" o "2") se debe ingresar a otro bucle
    en donde en cada iteración se pedirá una palabra. La cantidad de iteración
    (cantidad de palabras a solicitar) lo dejamos a gusto del alumno, intente que esa
    condición esté dada por una variable (ej: palabras_deseadas = 4)
    Cada palabra ingresada se debe ir almacenando en una lista de palabras, dicha
    lista la debe inicializar vacia y agregar cada nuevo valor con el método "append".
    Luego de tener las palabras deseadas almacenadas en una lista de palabras
    se debe proceder a realizar las siguientes tareas:

    Si se ingresa "1" por consola se debe obtener la palabra
    más grande por orden alfabético
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra
    más grande alfabeticamente.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?

    Si se ingresa "2" por consola se debe obtener la palabra
    con mayor cantidad de letras
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra con
    mayor cantidad de letras.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?
    
    NOTA: No se debe ordenar la lista de palabras, se debe obtener
    el máximo utilizando el mismos métodos vistos durante la clase
    (ejemplos_clase), tal como el ejercicio anterior. Ordenar una
    lista representa un problema mucho más complejo que solo
    buscar el máximo.

    NOTA: Es recomendable que se organice con lápiz y papel para
    hacer un bosquejo del sistema ya que deberá utilizar 3 bucles en total,
    1 - El bucle principal que hace que el programa corra hasta ingresar un "3"
    2 - Un bucle interno que corre hasta socilitar todas las palabras deseadas
        que se deben ir guardando en una lista
    3- Otro bucle interno que corre luego de que termine el bucle "2" que
       recorre la lista de palabras y busca la mayor según el motivo ingresado ("1" o "2")

    '''
    while True:
        lista =[] #inicio la lista para ingresar los valores
        orden = int(input("""
        1 - Obtener la palabra más grande por orden alfabético
        2 - Obtener la palabra más grande por cantidad de letras 
        3 - Salir del programa:\n"""))
        
        if orden == 1:
            cantidad_palabras = int(input("Ingrese la cantidad de palabras a utilizar:\n"))
            for i in range(cantidad_palabras):
                lista.append(str(input("Ingresar la palabra:\n"))) #Aqui ingreso las palabras a la lista
            ordenar(lista) # aqui llamo a una función para ordenar la lista
                            # lo hago mediante un reccorrido de ordenar por método burbuja
            print("La lista organizada por orden alfabetico es:", lista)
        else:
            if orden == 2:
                cantidad_palabras = int(input("Ingrese la cantidad de palabras a utilizar:\n"))
                for i in range(cantidad_palabras):
                    lista.append(str(input("Ingresar la palabra:\n")))
                letras(lista) # Llamo la función y ordeno por método burbuja
                print("La lista organizada de menor a mayor por cantidad de letras es:", lista)
            else:
                if orden == 3: #FIN del programa
                    print("Ha salido del programa")
                    break
                else: #vuelve al ciclo porque ha ingresado diferente a opciones 1, 2 o 3
                    print("Error, ha ingresado una opción que no se encuentra")
                    continue       
    
    
    
    


if __name__ == '__main__':
    print("Ejercicios de práctica")
    # ej1()
    #ej2()
    # ej3()
    # ej4()
    #ej5()