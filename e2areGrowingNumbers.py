"""
Victoria Ramos Rioja
10/09/23
ASIXc M03 UF1 A2
Descripció: Programa que detecta si tres números demanats han estat introduïts en ordre creixent.

e2
"""
entrada = input()
numeros = entrada.split()

numero1 = int(numeros[0])
numero2= int(numeros[1])
numero3= int(numeros[2])

if numero1 < numero2 < numero3:
    print("numeros crecientes")
else:
    print("numeros no crecientes")