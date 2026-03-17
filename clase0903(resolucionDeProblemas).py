#CICLO WHILE

#--
print("punto while: \n")


menu = """
menu del restaurante
1. Pizza
2. Hamburguesa
3. Gaseosa
4. Sopa
5. Menu del dia
6. Salir

"""

"""print(menu)"""


"""
se inicializa la variable opcion en cero para que pueda exitir la comparacion
en el ciclo 
"""


#---


"""

opcion = 0
while opcion != 6:

#como 0 es diferente de 6 entonces entra al bucle    
    opcion = int(input("ingrese la opcion del menu: "))
    
    #se ingresa la opcion como entrada entera
    #si cumple con los if, se ejecuta el if o condicion que cumpla
    
    #y como es un while, mientras que esa entrada se diferente de 6
    #se sigue ejecutando el ciclo

    if opcion == 1:
        print("has elegido la pizza. ")
    elif opcion == 2:
        print("has elegido la Hamburguesa. ")
    elif opcion == 3:
        print("has elegido la Gaseosa. ")
    elif opcion == 4:
        print("has elegido la Sopa. ")
    elif opcion == 5:
        print("has elegido la Menu del dia. ")
    
    #y cuando llega a se "opcion == 6" entonces se ejecuta esta condicion
    #y se rompe el ciclo
    elif opcion == 6:
        print("has elegido la Salir. ")
        break
    
    
    #aqui cualquier otro numero que no este contemplado en las condiciones anteriores
    #siempre se ejecuta este
    else:
        print("Ingrese una opcion valida. ")
    print(menu)        
"""


#---


print("punto suma total ")





menu = """
menu del restaurante
1. Pizza: 10,000$
2. Hamburguesa: 15,000$
3. Gaseosa: 5,000$
4. Sopa: 7,000$
5. Menu del dia: 11,000$
6. pagar

"""

"""
print(menu)


opcion = 0
total = 0
while opcion != 6:

   
    opcion = int(input("ingrese la opcion del menu: "))
    
 

    if opcion == 1:
        print("has elegido la pizza. ")
        total += 10000
    elif opcion == 2:
        print("has elegido la Hamburguesa. ")
        total += 15000
    elif opcion == 3:
        print("has elegido la Gaseosa. ")
        total += 5000
    elif opcion == 4:
        print("has elegido la Sopa. ")
        total += 7000
    elif opcion == 5:
        print("has elegido la Menu del dia. ")
        total += 11000
    
    
    elif opcion == 6:
        print(f"el total de su cuenta es :" + str(total))
        break
    
    
   
    else:
        print("Ingrese una opcion valida. ")
    print(menu)
"""

#---

print("punto total de tipos: \n")


menu = """
menu del restaurante
1. Pizza: 10,000$
2. Hamburguesa: 15,000$
3. Gaseosa: 5,000$
4. Sopa: 7,000$
5. Menu del dia: 11,000$
6. pagar

"""


print(menu)


opcion = 0
total = 0
totalPizza = 0
totalHamburguesa = 0
totalGaseosa = 0
totalSopa = 0
totalMenudia = 0

while opcion != 6:

    opcion = int(input("ingrese la opcion del menu: "))
    
 

    if opcion == 1:
        print("has elegido la pizza. ")
        total += 10000
        totalPizza += 10000
    elif opcion == 2:
        print("has elegido la Hamburguesa. ")
        total += 15000
        totalHamburguesa += 15000
    elif opcion == 3:
        print("has elegido la Gaseosa. ")
        total += 5000
        totalGaseosa +=5000
    elif opcion == 4:
        print("has elegido la Sopa. ")
        total += 7000
        totalSopa += 7000
    elif opcion == 5:
        print("has elegido la Menu del dia. ")
        total += 11000
        totalMenudia += 11000
    
    
    elif opcion == 6:
        print(f"el total de su cuenta es: " + str(total) + "$\n" + "total en hamburguesas: "
              + str(totalHamburguesa) + "$\n" + "total de pizzas: " + str(totalPizza) + "$\n"
              + "total gaseosas :" + str(totalGaseosa) + "$\n" + "total de sopa: " + str(totalSopa) + "$\n" 
              + "total de menus del dia: " + str(totalMenudia))
        break
    
    
   
    else:
        print("Ingrese una opcion valida. ")
    print(menu)




#CICLO FOR 

#CICLO FOR 

#dentro del rango el primero es el inicio"1" inicia en 1
#y el "11" es el final y el siempre va has desde incio "I"
#hasta un fin "n-1" por eso solpo imprime hasta 10
"""
print("punto for solo con inicio y fin :\n")
for x in range (1,11):
    print(x)
"""



##--
"""
print("punto FOR solo con el rango: \n")
#cuando solo se pone el rango, va desde la posicion "0" hasta "n-1", en paso de 1 en 1

for x in range (7):
    print(x)
"""



#--
"""
print("punto FOR con inicio fin y paso: \n")
#va desde "0" hasta "7", en paso "2", osea de 2 en 2
for x in range (0,7,2):
    print(x)
"""


#--
"""
print("ciclo for para la tabla de multiplicar: \n")

tabla=int(input("ingrese el numero del que quiere saber la tabla: \n"))

for x in range(1,11):
    resultado = x*tabla
    print(f"{x} x {tabla} = {resultado}")
"""


#--

print("punto for y while: \n")



i=1
while i < 11:
    print("tabla del: ",i)
    for x in range (1,11):
        resultado = i*x
        print(f"{i} x {x} = {resultado}") 
    i+=1

