"""
Victoria Ramos Rioja
10/09/23
ASIXc M03 UF1 A2
Descripció: dia sense IVA
e4
"""

importe = float(input("precio: "))
targeta = input("targeta?: ")

descuento = float((21*importe)/100)

if targeta == "si" and importe >= 100:
    importecondescuento = importe - descuento
    total = importecondescuento * 1.21
    print(round(total,2))