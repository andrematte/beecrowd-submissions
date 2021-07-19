# URI Online Judge 2172

while True:
    entrada = [int(i) for i in input().split()]

    if entrada[0] == 0 and entrada[1] == 0:
        break
    else: print(entrada[0] * entrada[1])