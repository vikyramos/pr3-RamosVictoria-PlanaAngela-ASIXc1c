"""
Victoria Ramos y Angela Plana
10/09/23
ASIXc M03 UF1 A2
Descripció: Programa que demana dos números si el primer és més gran o igual
que el segon els intercanvia. I torna a mostrar els valors per pantalla
e1
"""
entrada = input()
numeros = entrada.split()

num1 = int(numeros[0])
num2 = int(numeros[1])


#asignación multiple de la siguiente manera: variable_1 , variable_2 = variable_2 , variable_1.
if num1 >= num2:
    num1, num2 = num2, num1
    print(num1,num2)
else:
    print(entrada)
