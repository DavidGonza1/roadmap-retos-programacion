#Simple

def perimetro_cuadrado(lado):
  return (lado * 4)

resultado = perimetro_cuadrado(5)
print(f"El perimetro de un cuadrado con lado 5 es de {resultado}")

#Con argumentos variables
def sumar_todos(*n):
  return sum(n)
resultado = sumar_todos(5, 4, 8, 3)
print(f"La suma de los numeros es {resultado}")

#ejm2

def encontrar_maximo(*numeros):
  return max(numeros)
resultado = encontrar_maximo(5, 8, 6 ,9, 4, 2, 3, 4)
print(f"El maximo de los numeros es {resultado}")

#ejem3

from functools import reduce
def restar_valores(*valores):
  return reduce(lambda x, y: x - y, valores)
resultado = restar_valores( 5, 8, 9, 7, 4, 2)
print(f"La resta de los valores es de {resultado}")



# Función sencilla con argumentos

def area_triangulo(base, altura):
    return (base * altura) / 2

resultado = area_triangulo(20, 10)
print(f"El área del triángulo es {resultado}")

#Funciones anidadas

def objeto (x):
  def precio(e):
    def cantidad(c):
      return  e * c 
    return cantidad
  return precio

funcion_objeto = objeto("telefono")
funcion_precio = funcion_objeto(2500)
resultado = funcion_precio(2)
print(f" El '{funcion_objeto.__closure__[0].cell_contents}' tiene un valor de {resultado}")


# Ejemplo 2

def proyecto(costo_metros_cuadrados):
    def metros_cuadrados(numero_de_metros_cuadrados):
        def servicios_adicionales(costo_adicional_por_servicios):
            return (costo_metros_cuadrados * numero_de_metros_cuadrados) + costo_adicional_por_servicios
        return servicios_adicionales
    return metros_cuadrados

funcion_metros_cuadrados = proyecto(25)
funcion_servicios_adicionales = funcion_metros_cuadrados(50)
resultado = funcion_servicios_adicionales(55)

print(f"El costo total del proyecto es {resultado}")

# Ejemplo 3

def rectangulo(longitud):
    def anchura(ancho):
        def calcular_area():
            return longitud * ancho
        def calcular_perimetro():
            return 2 * (longitud + ancho)
        return calcular_area, calcular_perimetro
    return anchura

funcion_anchura = rectangulo(25)
calcular_area, calcular_perimetro = funcion_anchura(20)
area = calcular_area()
perimetro = calcular_perimetro()
print(f"El área del rectángulo es {area}")
print(f"El perímetro del rectángulo es {perimetro}")



# Ejemplo 4

import math  # Importar el módulo math para usar el valor de pi

def cilindro(radio_cilindro):
    def altura(altura_cilindro):
        def calcular_volumen():
            return math.pi * radio_cilindro ** 2 * altura_cilindro  # Ecuación completa para calcular el volumen
        def calcular_superficie():
            return 2 * math.pi * radio_cilindro * altura_cilindro + 2 * math.pi * radio_cilindro ** 2  # Ecuación completa para calcular la superficie
        return calcular_volumen, calcular_superficie
    return altura

funcion_altura = cilindro(5)
calcular_volumen, calcular_superficie = funcion_altura(10)
volumen = calcular_volumen()
superficie = calcular_superficie()
print(f"El volumen del cilindro es {volumen}")
print(f"La superficie del cilindro es {superficie}")


# Definición de una variable global
variable_global = "Soy una variable global"

def funcion_de_prueba():
    # Definición de una variable local
    variable_local = "Soy una variable local"
    print(f"Dentro de la función: {variable_local}") 
    print(f"Dentro de la función: {variable_global}")

funcion_de_prueba()

# Acceso a la variable global fuera de la función
print(f"Fuera de la función: {variable_global}")

# Intento de acceso a la variable local fuera de la función (esto causará un error)
try:
    print(f"Fuera de la función: {variable_local}")
except NameError as e:
    print(f"Error: {e}")


# Función que demuestra el uso de variables locales
def funcion_local():
    variable_local = "Soy una variable local"
    print(f"Dentro de la función: {variable_local}") 

funcion_local()

# Intento de acceso a la variable local fuera de la función (esto causará un error)
try:
    print(f"Fuera de la función: {variable_local}")
except NameError as e:
    print(f"Error: {e}")

# Definición de una variable global
variable_global = "Soy una variable global"

def mi_funcion():
    print(f"Dentro de la función: {variable_global}")

mi_funcion()
# Esto funcionará y mostrará: Soy una variable global
print(f"Fuera de la función: {variable_global}")
# Esto también funcionará y mostrará: Soy una variable global


"""
EXTRA
"""
def imprimir_multiples(texto1, texto2):
    conteo_numeros = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(texto1 + texto2)
        elif i % 3 == 0:
            print(texto1)
        elif i % 5 == 0:
            print(texto2)
        else:
            print(i)
            conteo_numeros += 1
    return conteo_numeros
# Ejemplo de uso
resultado = imprimir_multiples("M3", "M5")
print(f"El número de veces que se imprimieron números es {resultado}")








  


  

