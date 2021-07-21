# URI Online Judge 1930

entrada = [int(i) for i in input().split()]
    
saida = entrada[-1] + sum(entrada[:3]) - len(entrada) + 1

print(saida)