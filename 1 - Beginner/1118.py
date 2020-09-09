# URI Online Judge 1117
nota1, nota2 = -1, -1
continuar = 1

while continuar == 1:

    nota1, nota2 = -1, -1

    while nota1 < 0 or nota1 > 10:
        nota1 = float(input())
        if nota1 < 0 or nota1 > 10:
            print("nota invalida")


    while nota2 < 0 or nota2 > 10:
        nota2 = float(input())
        if nota2 < 0 or nota2 > 10:
            print("nota invalida")

    print("media = {0:.2f}".format((nota1+nota2)/2))

    continuar = -1
    while continuar !=1 and continuar !=2:
        print("novo calculo (1-sim 2-nao)")
        continuar = int(input())
