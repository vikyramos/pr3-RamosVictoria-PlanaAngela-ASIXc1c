data = input("Escriu una data en format DD/MM/AAAA: ")

dia = int(data.split("/") [0])
mes = int(data.split("/") [1])
anys = int(data.split("/") [2])

#año bisiesto
if anys %100 == 0:
    (anys/100) / 4
if (anys) %4 == 0  and mes == 2 and dia <=29:
    print("Data valida")

#if dia in range(1,31 + 1) and mes



