
#LISTAS /LIST

my_list = [ 1 , 2, 3, 4, 5, 6, 7, 8]
print(my_list)

"""
OPERACIONES BASICAS
"""
"""
INSERCION
"""

#APPEND / AGREGA UN ELEMENTO AL FINAL DE LA LISTA
my_list.append(9)
print(my_list) #Resultado/salida : [ 1 , 2, 3, 4, 5, 6, 7, 8, 9]

#INSERT/ INSERTA UN ELEMENTO EN UNA POSICION ESPECIFICA
my_list.insert(  5, 'N')
print(my_list) # salida : [ 1 , 2, 3, 4, 5, N, 6, 7, 8, 9]

"""
BORRADO
"""

#REMOVE / ELIMINA LA PRIMERA OCURRENCIA DE UN ELEMENTO
my_list.remove('N')
print(my_list) #salida : [ 1 , 2, 3, 4, 5, 6, 7, 8, 9]

#POP / ELIMINA Y RETORNA EL ELEMTO A UNA POSICION ESPECIFICA
elemento_eliminado = mi_list.pop(5)
print(my_list) #[ 1 , 2, 3, 4, 5, 7, 8, 9]
print(f"Elemento eliminado: {elemento_eliminado}") #salida : Elemento eliminado : 6

#DEL / ELIMINA EL ELEMNTO EN UNA POSICION ESPECIFICA

del my_list[ 1 ]
print(my_list) #salida [ 1 , 3, 4, 5, 7, 8, 9]

"""
ACTUALIZACION
"""
my_list[1] = 10
print(my_list) #salida [ 1 , 10, 4, 5, 7, 8, 9]


"""
ORDENACION
"""

#SORT / ORDENA LA LISTA EN ORDEN ASCENDENTE
my_list.sort()
print(my_list) #salida [ 1, 4, 5, 7, 8, 9, 10]

#SORT /ORDENA LA LISTA EN ORDEN DESCENDENTE USANDO EL PARAMETRO REVERSE=TRUE
my_list.sort(reverse=True)
print(my_list) #salida [10, 9, 8, 7, 5, 4, 1]

#SORTED /RETORNA UNA NUEVA LISTA ORDENADA, SIN MODIFICAR LA LISTA ORIGINAL
new_list = sorted(my_list)
print(new_list) #salida [ 1, 4, 5, 7, 8, 9, 10]
print(my_list)  #salida [10, 9, 8, 7, 5, 4, 1]

"""
TUPLAS
son una estructura de datos que permite almacenar múltiples elementos en una sola variable.
A diferencia de las listas, las tuplas son inmutables, lo que significa que no se pueden
cambiar una vez creadas.
"""

#La sintaxis es la siguiente : para crear una tupla, se utilizan paréntesis () y se separan los elementos por comas.
my_tulpa (1, 2, 3, 4, 5, 6)
print(my_tupla)

#Acceso a elementos, puedes acceder a los elementos de una tupla utilizando indeces.
print(my_tupla[0]) # Accede al primer elemento, salida:1
print(my_tupla[2]) # Accede al primer elemento, salida:3

"""
OPERACIONES
BASICAS
"""

#LEN() /PARA OBTENER EL NUMERO DE ELEMENTOS DE UNA TUPLA
print(len(my_tulpa)) #salida : 6

#CONCATENACION / PARA CONCATENAR DOS O MAS TUPLAS UTILIZANDO EL OPERADOR +
tupla1 = (1, 2, 3, 4)
tupla2 = (5, 6, 7, 8)
tupla_concatenada = tupla1 + tupla2 # tupla_concatenada =(1, 2, 3, 4, 5, 6, 7, 8)

#REPETIR TULPA/ UTILIZANDO EL OPERADOR *
tupla_repetida = tulpa2 * 2
print(tupla_repetida) # salida: (5, 6, 7, 8, 5, 6, 7, 8)

#IN / USAMOS EL OPERADOR IN PARA VER SI UN ELEMENTO ESTA EN NUESTRA TULPA 
print(8 in my_tupla) # FALSE
print(4 in my_tupla) # TRUE

#DESEMPAQUETADO DE TULPAS / PUEDES ASIGNAR VALORES DE UNA TUPLA A VARIABLES INDIVIDUALES

a, b, c, d, e, f = my_tupla
print(a) # salida 1
print(b) # salida 2
print(c) # salida 3
print(d) # salida 4
print(e) # salida 5
print(f) # salida 6

"""
METODOS DE TUPLAS
LAS TULPAS TIENEN DOS METODOS INTEGRADS PRINCIPALES
ESTOS SON:
"""

#COUNT() /Devuelve el numero de veces que un valor especificado aparece en la tupla

my_new_tupla = ("carro", "telefono", "cama", "telefono", "silla", "telefono", "cable", "audifono", "telefono")
print(my_new_tupla.count("telefono")) # Salida: 4 #salida : 4

#INDEX() / DEVUELVE EL INDICE DEL PRIMER ELEMENTO CUYO VALOR ES IGUAL A UN VALOR ESPECIFICADO
print(my_new_tupla.index("cama")) # Salida: 2

'''
AHORA CONTINUAMOS CON LOS CONJUNTOS(SETS)
ESTOS SON COLECCIONES DESORDENADAS DE ELEMENTOS UNICOS.
No permiten duplicados y son mutables, 
lo que significa que puedes modificar sus elementos después de crearlos.
'''

my_conjunto = {1, 2, 3, 4, 5, 6}
print(my_conjunto)

#Tambien se puede crear un conjunto usando la funcion set()

my_conjunto = set([1,2,3,4,5,6])
print(my_conjunto)

"""
INSERCION
"""

#ADD / AGREGA UN ELEMENTO AL CONJUNTO
my_conjunto.add(7)
print(my_conjunto) #salida: {1, 2, 3, 4, 5, 6, 7}

"""
BORRADO
"""

#REMOVE / ELIMINA UN ELEMENTO ESPECIFICO DEL CONJUNTO
my_conjunto.remove(5)
print(my_conjunto) #salida {1, 2, 3, 4, 6, 7}

#DISCARD / ELIMINA UN ELEMENTO ESPECIFICO DEL CONJUNT OSIN GENERAR ERROR SI EL ELEMENTO NO EXISTE
my_conjunto.discard(8)
print(my_conjunto)  # No hace nada ya que 8 no esta en el conjunto

#POP / ELIMINA Y DEVUELVE UN ELEMENTO ARBITRIARIO DEL CONJUNTO
elemento_eliminado = my_conjunto.pop()
print(my_conjunto)
print(f"Elemento eliminado: {elemento_eliminado}")

"""
operaciones
"""

#UNION / COMBINA DOS CONJUNTOS

conjunto1= {1, 2, 3}
conjunto2= {3, 4, 5, 6}
conjunto_union = conjunti1.union(conjunto2)
print(conjunto_union) 

#INTERSECTION / ENCUENTRA LOS ELEMENTOS COMUNES ENTRE DOS CONJUNTOS
conjunto_intersection = conjunto1.intersection(conjunto2)
print(conjunto_intersection) # Salida: {3}

#DIFFERENCE /ENCUENTRA LOS ELEMENTOS QUE ESTAN EN UN CONJUNTO PERO NO EN EL OTRO
conjunto_diferencia = conjunto1.difference(conjunto2)
print(conjunto_diferencia)  # Salida: {1, 2}

"""
DICCIONARIOS/ DICTIONARIES
Son colecciones desordenadas de pares clave-valor.
Las claves deben ser unicas y inmutables,
mientras que los valores pueden ser de cualquier tipo
"""

#Creacion
my_diccionario = {'a': 1, 'b': 2, 'c': 3}
print(my_diccionario)

#otra forma de crearlo es usando la funcion dict()
my_diccionario = dict(a=1, b=2, c=3)
print(my_diccionario)

"""
INSERCION Y ACTUALIZACION
"""

#ASIGNACION / AGREGA UN NUEVO PAR CLAVE-VALOR O ACTUALIZA EL VALOR DE UNA CLAVE EXISTENTE

my_diccionario['d'] = 4
my_diccionario['a'] = 9
print(mi_diccionario)  # Salida: {'a': 9, 'b': 2, 'c': 3, 'd': 4}

#BORRADO/ DEL, ELIMINA UN PAR CLAVE-VALOR ESPECIFICO

del my_dicionario['a']
print(mi_diccionario) # Salida: {'b': 2, 'c': 3, 'd': 4}

#POP / ELIMINA Y DEVUELVE EL VALOR ASOCIADO A UNA CLAVE ESPECIFICA
valor_eliminado = my_diccionario.pop('c')
print(my_diccionario)  # Salida: {'b': 2, 'd': 4}
print(f"Valor eliminado: {valor_eliminado}")  # Salida: 3

#POPITEM / ELIMINA Y DEVUELVE EL ULTIMO PAR CLAVE-VALOR DEL DICCIONARIO

clave_valor_eliminado = my_diccionario.popitem()
print(my_diccionario)
print(f"Clave y valor eliminados: {clave_valor_eliminado}")

'''
ACCESO A VALORES
'''
valor_a = my_diccionario['a', 'No encontrado']
print(valor_a)  # Salida: No encontrado

#TAMBIEN PODEMOS UTILIZAR EL METODO get() PARA ACCEDER A LOS VALORES

valor_b = my_diccionario.get('b', 'No encontrado')
print(valor_b) # Salida: 2

"""
EXTRA --------------------------------------------------------------------------------------------------------------------------------
"""

agenda = {}


#Funcion para insertar un contacto
def insertar_contacto( nombre, telefono):
  if len(telefono) > 11 or not telefono.isdigit():
      print("Numeno de telefono no valido.")
  else:
    agenda[nombre] = telefono
    print(f"Contacto {nombre} añadido con exito.")
    
#Funcion para buscar un contacto
def buscar_contacto(nombre):
  if nombre in agenda:
     print(f" {nombre}: {agenda[nombre]}")
  else:
      print("Contacto no encontrado.")

#Funcion para actualizar un contacto
def actualizar_contacto(nombre, nuevo_telefono):
    if nombre in agenda:
        if len(nuevo_telefono) > 11 or not nuevo_telefono.isdigit():
            print("Número de teléfono no válido.")
        else:
            agenda[nombre] = nuevo_telefono
            print(f"Contacto {nombre} actualizado con éxito.")
    else:
        print("Contacto no encontrado.")

#Funcion para eliminar un contacto
def eliminar_contacto(nombre):
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado con éxito.")
    else:
        print("Contacto no encontrado.")
      

#Menu 
def menu():
    while True:
        print("\nAgenda de Contactos")
        print("1. Insertar Contacto")
        print("2. Buscar Contacto")
        print("3. Actualizar Contacto")
        print("4. Eliminar Contacto")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre = input("Nombre del contacto: ")
            telefono = input("Número de teléfono: ")
            insertar_contacto(nombre, telefono)
        elif opcion == '2':
            nombre = input("Nombre del contacto: ")
            buscar_contacto(nombre)
        elif opcion == '3':
            nombre = input("Nombre del contacto: ")
            nuevo_telefono = input("Nuevo número de teléfono: ")
            actualizar_contacto(nombre, nuevo_telefono)
        elif opcion == '4':
            nombre = input("Nombre del contacto: ")
            eliminar_contacto(nombre)
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 5.")

# Ejecutar el menú
menu()











