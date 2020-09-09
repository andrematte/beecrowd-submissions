# URI Online Judge 1115

X,Y = 1,1

while X!=0 and X!=0:
    Entrada = input()
    X = int(Entrada.split()[0])
    Y = int(Entrada.split()[1])

    if X>0 and Y>0:
        print("primeiro")
    elif X>0 and Y<0:
        print("quarto")
    elif X<0 and Y>0:
        print("segundo")
    elif X<0 and Y<0:
        print("terceiro")