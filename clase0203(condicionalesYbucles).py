"""

##impresion con formato

#el formato es una forma de hacer una impresion añadiendo 
#el valor del parametro señalado  

print("punto 1:\n")

a = 1
b = 2

suma = a + b
#aqui se añade el formato con la "f" antes de la cadena de texto y dentro de la cadena se usa
#{} para llamar el valor del parametro señalado

print(f"el numero {suma}, es el resultado de sumar \n {a} \n y \n {b} ")

#el salto de linea dentro de las comillas de la cadena de texto
#no necesitan las comillas

print("punto 2:\n")
#--//


#se puede escribir las variables y sus valores en una sola asignacion
#a esto se le llama --MULTIPLES ASIGNACIONES--


num1, num2, num3 = 4, 5, 7
print(f"el numero 1 es: {num1}\nel numero 2 es: {num2}\nel numero 3 es: {num3} ")
"""


"""
#--//
print("punto 3:\n")

nombre1 = input("ingrese su nombre: ")
edad1 = int(input("ingrese su edad: "))

#como no se puede concatenar enteros con strings se castea el valor int a string

print("hola" + nombre1 + ", tienes" + str(edad1) "años")

"""

#------

"""

print("punto calculadora:" )

nombre1 = input ("ingrese su nombre: ") 

numero1 = int(input("ingrese su primer numero: "))
numero2 = int(input("ingrese su segundo numero: "))

#se puede realizar la operacion dentro del texto sin asingar la operacion
#a una variable, asi de la siguiente manera

# SUMA
print (" hola " + nombre1 + " la suma de los dos numeros es " + str(numero1+numero2) + "\n")
# RESTA
print("la resta de los numeros es :" + str(numero1-numero2) + "\n")
# MULTIPLICACION
print("el resultado de la multiplicacion es: " + str(numero1*numero2) + "\n")


# DIVISION
#en esta caso de la division se puede controlar
#la cantidad de decimales que queremos imprimir, añadimos primero el formato 
# "f{@param :.#ndF}" para la cadena y luego la instruccion .(cantidadDecimales)f
#para ello hay que asignar la operaciona a una variable y seguido de una " , "
#no es posible hacerlo concatenando con " + "
division = numero1/numero2
print(f"el resltado de la division es: ",  f"{division:.2f} ")


# DIVISION ENTERA
print("el resultado de la division entera es: " + str(numero1//numero2) + "\n")
# POTENCIACION
print("el resultado de la potaciacion es: " + str(numero1**numero2) + "\n")
# MODULO
print("el resultado del modulo es: " + str(numero1%numero2) + "\n")
"""

#-----


"""s
print("punto area de un circulo: \n")

print("vamos a calcular el area de un circulo \n")

radio = int(input("ingrese el radio del circulo: "))
PI = 3.1416
# π r²
area = PI*(radio**2)
#aqui manejamos las cantidad de decimales a imprimir con f"{@param:.#f}"
print("el area del circulos es: ", f"{area:.3f}")

"""

#---

"""
print("punto area del triangulo: \n")

print ("vamos a calcular el area del triangulo... \n")

altura = int(input("ingrese la altura del triangulo: "))
base = int(input("ingrese la base del triangulo: "))

areaTriangulo = (base*altura)/2

print ("el area del triangulo es: ", f"{areaTriangulo:.3f}")
"""

#---


print("punto calcular salario \n")
print("vamos a calcular el salario del empleado \n")

nombreEmpleado1=input("ingrese el nombre del empleado 1: ")
valorHora1=int(input("ingrese el valor por hora del empleado 1: "))
horaTrabajada1=float(input("cuantas horas trabajo el empleado en la semana 1: "))

nombreEmpleado2=input("ingrese el nombre del empleado 2: ")
valorHora2=int(input("ingrese el valor por hora del empleado 2: "))
horaTrabajada2=float(input("cuantas horas trabajo el empleado en la semana 2: "))

nombreEmpleado3=input("ingrese el nombre del empleado 3: ")
valorHora3=int(input("ingrese el valor por hora del empleado 3: "))
horaTrabajada3=float(input("cuantas horas trabajo el empleado en la semana 3: "))

print(f"el empleado {nombreEmpleado1}, gano esta semana " + str(valorHora1*horaTrabajada1) + "\n")
print(f"el empleado {nombreEmpleado2}, gano esta semana " + str(valorHora2*horaTrabajada2) + "\n")
print(f"el empleado {nombreEmpleado3}, gano esta semana " + str(valorHora3*horaTrabajada3) + "\n")

nominaTotal = (valorHora1*horaTrabajada1) + (valorHora2*horaTrabajada2) + (valorHora3*horaTrabajada3)
print("el valor total de la nomina de los empleados en esta semana es de " + str(nominaTotal) + "$ pesos")