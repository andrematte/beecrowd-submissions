# URI Online Judge 1234
import operator

while True:
    try:
        entrada = input()
        saida = ''
        upper = True

        for i in range(len(entrada)):
            if entrada[i] == ' ':
                saida += ' '
            elif upper:
                saida += entrada[i].upper()
                upper = operator.not_(upper)
            elif not upper:
                saida += entrada[i].lower()
                upper = operator.not_(upper)
                
        print(saida)
    except EOFError:
        break