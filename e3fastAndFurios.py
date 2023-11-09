"""
Victoria Ramos Rioja
10/09/23
ASIXc M03 UF1 A2
Descripció: Volem un programa que calculi la velocitat instantània i la velocitat mitjana. Cal demanar velocitat inicial (m/s), l'acceleració (m/s2) i el temps.
Si la velocitat instantània és inferior o igual a 0, has d'indicar que està parat i no pots calcular la velocitat mitjana.
velocitat instantània = velocitat inicial + acceleració * temps
velocitat mitjana = (velocitat inicial + velocitat instantània )/2

e3
"""

velocidadinicial = float(input("velocidad: "))
acceleracion = float(input("acceleración: "))
tiempo = float(input("tiempo: "))

#acceleracionportiempo= acceleracion*tiempo

velocidad_instantanea= velocidadinicial + (acceleracion*tiempo)

print(velocidad_instantanea)

if velocidad_instantanea <=0:
    print("Esta parado")
else:
    velocidad_media = (velocidadinicial + velocidad_instantanea)/2
    print(velocidad_media)
