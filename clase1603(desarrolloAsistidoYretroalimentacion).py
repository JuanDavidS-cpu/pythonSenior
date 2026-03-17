"""
Ejercicio práctico (2 horas)
Sistema de Gestión Básica de Estudiantes
Contexto

Una universidad quiere desarrollar un pequeño programa en Python que permita registrar estudiantes y evaluar su estado académico de forma simple desde la terminal.

Tu tarea será desarrollar un script en Python estructurado con funciones que permita ingresar información de estudiantes, calcular su promedio y mostrar su estado académico.

Requisitos del programa

El programa debe permitir:

1️⃣ Registrar estudiantes
2️⃣ Calcular el promedio de tres notas
3️⃣ Determinar el estado del estudiante
4️⃣ Permitir registrar varios estudiantes usando un menú
5️⃣ Mostrar un resumen final

Reglas del sistema

Para cada estudiante se debe ingresar:

Nombre

Edad

Nota 1

Nota 2

Nota 3

El programa debe calcular:

promedio = (nota1 + nota2 + nota3) / 3

Y determinar el estado académico:

Promedio	Estado
>= 4.0	Aprobado
>= 3.0 y < 4.0	En recuperación
< 3.0	Reprobado
Estructura obligatoria del programa

El programa debe tener al menos estas funciones:

1️⃣ Función para registrar estudiante
def registrar_estudiante():

Debe pedir:

nombre

edad

3 notas

Debe retornar los datos.

2️⃣ Función para calcular promedio
def calcular_promedio(n1, n2, n3):

Debe retornar el promedio.

3️⃣ Función para determinar estado
def evaluar_estado(promedio):

Debe retornar:

"Aprobado"

"En recuperación"

"Reprobado"

4️⃣ Menú principal con bucle

El programa debe mostrar un menú como este:

1. Registrar estudiante
2. Salir

Debe usar un while para permitir registrar varios estudiantes.

Ejemplo de salida esperada
===== SISTEMA DE ESTUDIANTES =====

Ingrese el nombre del estudiante: Ana
Ingrese la edad: 20
Ingrese nota 1: 4.5
Ingrese nota 2: 3.8
Ingrese nota 3: 4.2

Promedio del estudiante: 4.17
Estado académico: Aprobado
Validaciones mínimas

El programa debe validar:

Que las notas estén entre 0 y 5

Que la edad sea mayor que 0

Si los datos no son válidos, debe pedirlos nuevamente.

Parte final (obligatoria)

Al terminar el programa debe mostrar:

Total de estudiantes registrados: X
Promedio general del grupo: X

"""
#creo una lista
Estudiantes=[]
def RegistrarEstudiante():
    #creo un diccionario para ingresar cada estudiante en un diccionario
    estudiante={}
    nombreEstudiante = input("ingrese el nombre del estudiante: ")

    #while para contemplar valor que no estan en el rango
    edad = int(input(f"\n"+f"ingrese la edad de {nombreEstudiante}: "))
    while edad <= 0:
        print("ingrese un rango de edad mayor a cero") 
        #se pide una nueva entrada para que no genere bucle infinito
        #si no se pide nueva entrada, edad queda en el ultimo valor y nunca cambia
        edad = int(input(f"ingrese la edad de {nombreEstudiante}: "))

    nota1 = float(input(f"ingrese la primer nota de {nombreEstudiante}: "))
    while nota1 < 0 or nota1 > 5:
        print("ingrese un rango de nota entre 0 y 5 ") 
        nota1 = float(input(f"ingrese la primer nota de {nombreEstudiante}: "))

        
    nota2 = float(input(f"ingrese la segunda nota de {nombreEstudiante}: "))
    while nota2 < 0 or nota2 > 5:
        print("ingrese un rango de nota entre 0 y 5 ") 
        nota2 = float(input(f"ingrese la segunda nota de {nombreEstudiante}: "))

    nota3 = float(input(f"ingrese la tercer nota de {nombreEstudiante}: "))
    while nota3 < 0 or nota3 > 5:
        print("ingrese un rango de nota entre 0 y 5 ") 
        nota3 = float(input(f"ingrese la tercer nota de {nombreEstudiante}:"+"\n"))


    
    estudiante["nombre"] = nombreEstudiante
    estudiante["edad"] = edad
    estudiante["nota1"] = nota1
    estudiante["nota2"] = nota2
    estudiante["nota3"] = nota3

    #el diccionario, lo ingreso a la lista, para que halla una lista de estudiantes
    Estudiantes.append(estudiante)

    return estudiante


def calcularPromedio (estudiante):
    
    Promedio = (estudiante["nota1"] + estudiante["nota2"] + estudiante["nota3"]) / 3
    estudiante["promedio"] = Promedio
    return Promedio

def estadoEstudiante(estudiante):
    if estudiante["promedio"] < 3:
        estado = "reprobado"
    elif estudiante["promedio"]>=3 and estudiante["promedio"] < 4 :
        estado = "En recuperacion"
    else:
        estado = "Aprobado"

    estudiante["estado"] = estado

    return estado



opcion = 0

while opcion != 3 :
    opcion = int(input("""
        seleccione una opcion: 
                       
        ===== SISTEMA DE ESTUDIANTES =====
            
        1. Registrar estudiante
        2. Mostrar lista de estudiantes
        3. Salir

        """))

    if opcion == 1:
        #se asigna a variables las funciones para que tome el ultimo diccionario creado
        estudiante = RegistrarEstudiante()
        promedio = calcularPromedio(estudiante)    
        estado = estadoEstudiante(estudiante)       
        print(f"el promedio de {estudiante['nombre']} fue de {promedio:.2f}")
        print(f"el estado academico de {estudiante["nombre"]} : {estado}")
            
    elif opcion == 2:
        for estudiante in Estudiantes:
            print(f"""nombre: {estudiante["nombre"]}, 
edad: {estudiante["edad"]}, 
nota 1: {estudiante["nota1"]},
nota 2: {estudiante["nota2"]},
nota 3: {estudiante["nota3"]}, 
promedio : {estudiante["promedio"]:.2f}                             
estado : {estudiante["estado"]}            
""")

    elif opcion == 3:
        contador = 0
        sumaPromedios = 0
        for estudiante in Estudiantes:
            #un contador para cada estudiante recorrido en Estudiantes
            contador += 1
            sumaPromedios += estudiante['promedio']
            #y cada promedio se asigna a sumapromedio
        promedioTotal = sumaPromedios/contador
        #aqui es el total de la sumapromedio / contador(numero de estudiantes)
        print("!! GRACIAS POR USAR EL SOFTWARE¡¡\n")
        print(f"hay {contador} estudiantes registrados")
        print(f"el promedio general de la clase es de {promedioTotal:.2f}")
        
    else:
        print("INGRESE UNA OPCION VALIDA")





        




















