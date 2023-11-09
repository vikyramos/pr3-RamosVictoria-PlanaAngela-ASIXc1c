"""
Victoria Ramos i Angela PLana
7/11/2023
ASIXc M03 UF1 RA3

Descripció:L'usuari introdueix la lletra del tipus d'habitatge i número de m3  d'aigua gastats.
Mostrar per pantalla el preu total de la factura de l’aigua. Arrodonit a 2 decimals

"""
habitatge = input("Introdueixi el tipus d'habitatge: ")
aigua = float(input("Introdueixi els m³ d'aigua gastats: "))

tram1 = aigua * 0.5849
tram2 = aigua * 1.1699
tram3 = aigua * 1.7548
tram4 = aigua * 2.3397
tram5 = aigua * 2.9246

habitatge = habitatge.replace("A", "2.46")
habitatge = habitatge.replace("B", "6.40")
habitatge = habitatge.replace("C", "7.25")
habitatge = habitatge.replace("D", "11.21")
habitatge = habitatge.replace("E", "12.10")
habitatge = habitatge.replace("F", "17.28")
habitatge = habitatge.replace("G", "28.01")
habitatge = habitatge.replace("H", "40.50")
habitatge = habitatge.replace("I", "61.31")





if aigua >= 0 and aigua < 7:
    print(round(tram1 + float(habitatge), 2))
elif aigua >= 7 and aigua < 10:
    print(round(tram2 + float(habitatge), 2))
elif aigua >= 10 and aigua < 16:
    print(round(tram3 + float(habitatge), 2))
elif aigua >= 16 and aigua < 18:
    print(round(tram4 + float(habitatge), 2))
elif aigua >= 18 :
    print(round(tram5 + float(habitatge), 2))
else:
    print("Error, introdueix el tipus d'habitge en majuscual i el número de m³")