# URI Online Judge 2057

entrada = [int(i) for i in input().split()]
saida = sum(entrada)

if saida > 23:
    saida -= 24

if saida < 0:
    saida += 24
    
print(saida)