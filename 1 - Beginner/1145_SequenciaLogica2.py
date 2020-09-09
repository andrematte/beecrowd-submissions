# URI Online Judge 1144

Entrada = input()
X = int(Entrada.split()[0])
Y = int(Entrada.split()[1])

count = 1

while count < Y:

    Sequencia = ''

    for x in range(0,X):
        if count <= Y and x == 0:
            Sequencia = Sequencia + "{}".format(count)
            count += 1
        elif count <= Y:
            Sequencia = Sequencia + " {}".format(count)
            count += 1

    print(Sequencia)
