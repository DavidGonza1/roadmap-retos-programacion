
#ARITMETICOS

x = 5
y = 10

#SUMA
suma = x + y #15
print(f"suma: 5 + 10 = {5 + 10}")

#RESTA
resta = x - y  #5
print(f"resta: 5 - 10 = {5 - 10}")

#MULTIPLICACION
multiplicaion = x * y # 50
print(f"multiplicacion: 5 * 10 = {5 * 10}")
#DIVISION
division = x / b  #0.5
print(f"division: 5 / 10 = {5 / 10}")

#DIVISION DE ENTERO

division_integer = x // b  
print(f"division de entero: 5 // 10 = {5 // 10}")

#MODULO, es el resto de la division
modulo = a % b # 5
print(f"modulo: 5 % 10 = {5 % 10}")

#EXPONENCIACION
exponenciacion = a ** b #9765625
print(f"modulo: 5 ** 10 = {5 ** 10}")


#COMPARACION, esto compara dos valores y los devuelve con un valor booleano


b = 10
c= 12

#Igual a 
igual = (b == c) #False
print(f"igualdad: 10 == 12 es {10 == 12}")

#Diferente a
diferente = (b != c) #True
print(f"desigualdad: 10 != 12 es{10 != 12}")

#Mayor que 
mayor= ( b > c ) #False
print(f"mayor que: 10 > 12 es {10 > 12}")

#Menor que 
menor = ( b < c) #True
print(f"menor que: 10 < 12 es {10 < 12}")

#Mayor o igual que 
mayor_igual = ( b >= c) #False
print(f"mayor o igual que : 10 >= 12 es {10 >= 12}")

#Menor o igual que
menor_igual = ( b <= c) #True
print(f"menor o igual que : 10 <= 12 es {10 <= 12}")

#OPERADORES LOGICOS, combinan expresiones booleanas

A = True
B = False

#AND, el operador devuelve true si ambos expresiones son true. Devuelve False si una de las expresiones son False
ejemplo = a and b #False, porque al menos uno de las expresione es False
print(f("AND: 10 + 3 == 13 and 15 + 2 == 17 es {10 + 3 == 13 and 15 + 2 == 17}")

#OR, el operador or devuelve True si al menos una de las expresiones es True. Devuelve False solo si ambas expresiones son False.
segundo_ejemplo = a or b #True, porque almenos uno de las expresiones es True
print(f("OR: 10 + 3 == 12 and 8 + 2 == 10 es {10 + 3 == 12 and 8 + 2 == 10}")
      
#NOT, El operador not invierte el valor de la expresión. Si la expresión es True, devuelve False y viceversa.
e = True
f = False
first_example = not e #False, porque 'not' invierte el valor de True
second_example = not f #True, porque 'not' invierte el valor de False
print(f("NOT: 20 - 15 == 5 es {20 - 15 == 5}")

#OPERADORES DE ASIGNACION, estos se utilizan para asignar valores a las variables
#Asignacion
a = 5
print(a)

a = 10 # a ahora es 10
print(a)

#Suma y asignacion
a += 5 # a ahora es 15
print(a)

#Resta y asignacion
a -= 5 # a ahora es 10
print(a)

#Multiplicacion y asignacion
a *= 5 # a ahora es 50
print(a)

#Division y asignacion
a /= 10 # a ajpra es 5.0
print(a)

#Modulo y asignacion
a %= 4 # a ahora es 2.0
print(a)

#Exponenciacion y asignacion
a **= 3 # a ahora es 8.0
print(a)


#OPERADORES DE IDENTIDAD
#estos se utilizan para comparar la identidad de los objetos

#IS
#El operador is comprueba si dos variables hacen referencia al mismo objeto en memoria
#Devuelve True si las variables son el mismo objeto y False en caso contrario.
f = [ 1, 2, 3 ]
g = f
h = [ 1, 2, 3]
is_operador= (f is g) #True, porque uno hace referencia al mismo objeto
is_operador1=(f is h) #False, aunque tienen el mismo contenido, no son el mismo objeto
#Otro ejemplo
b = 1.0
c = 1.0
print(f" b is c es {b is c}") # False 


#IS NOT
#comprueba si dos variables NO hacen referencia al mismo objeto en memoria.
#Devuelve True si las variables no son el mismo objeto y False en caso contrario.
a = [1, 2, 3]
b = a
c = [1, 2, 3]
is_not_operador = (a is not b) #False, porque hacen referencia al mismo objeto
is_not_operador2= (a is not c) #True, porque a y c son diferentes
x= 5.0
y= 4.2
print(f" x is not y es {x is not y}")


#OPERADORES DE PERTENENCIA
#Estos operadores se utilizan para comprobar si un valor está presente en una secuencia.

objetos = ["manzana", "celular", "balon"]

#IN (dentro de)
in_operador =("celular" in objetos) #True
print(f"celular in objetos = { in_operador}")

#NOT IN (no esta dentro de)
not_in_operador = ("cargador" not in objetos) #True
print(f"cargador not in objetos = { not_in_operador}")

#Otro ejemplo, con cadenas de texto

mensaje = " Hola, bienvenidos"

in_mensaje = ("bienvenidos" in mensaje) #True, porque esta dentro de mensaje
print(f"bienvenidos in mensaje = { in_mensaje}")

not_in_mensaje = ( "mundo" not in mensaje) #true, porque no esta dentro de mensaje
print(f"mundo not in mensaje = {not_in_mensaje}")

#OPERADORES DE BIT

numero1 = 10 #1010
numero2 = 3 #0011
print(f"AND: 10 & 3 = {10 & 3}") # 0010
print(f"OR: 10 | 3 = {10 | 3}") # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}") # 1001
print(f"NOT: 10 ~ 3 = {~10}") 
print(f"DESPLAZAR A LA DERECHA: 10 >> 2 = {10 >> 2}") # 0010
print(f"DESPLAZAR A LA IZQUIERDA: 10 << 2 = {10 << 2}") # 101000


"""
ESTRUCTURAS DE CONTROL
"""

#CONDICIONALES

objeto = carro

if objeto == "carro": 
  print("objeto es un 'carro'") 
else: print("objeto no es un 'carro'")

#Iterativas

for b in range(20):
  print(b)

c = 10

while c <= 25:
  print(c)
  c += 1

# Manejo de excepciones
try:
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Se ha finalizado el manejo de excepciones")

"""
EXTRA
"""
for numero in range(10, 56):
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        print(numero)





 




