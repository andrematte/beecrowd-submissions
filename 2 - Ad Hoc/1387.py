# URI Online Judge 1387

while True:
    entrada = [int(i) for i in input().split()]
    esq, dir = entrada[0], entrada[1]
    
    if esq == 0 and dir == 0:
        break
    
    print(esq + dir)