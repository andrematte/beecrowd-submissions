# URI Online Judge 1113

X = 0
Y = 1

while X!=Y:

    Entrada = input()

    X = int(Entrada.split()[0])
    Y = int(Entrada.split()[1])

    if X < Y:
        print("Crescente")
    elif Y < X:
        print("Decrescente")
