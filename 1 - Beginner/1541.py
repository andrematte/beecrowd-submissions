# URI Online Judge 1541
from math import sqrt

while True:
    entrada = input()
    if entrada == '0': break

    entrada = [int(i) for i in entrada.split()]
    A, B, C = entrada[0], entrada[1], entrada[2]
    
    m2 = A * B
    terreno = m2 * (100/C)
    lado_terreno = sqrt(terreno)
    
    print(int(lado_terreno))
    
    
    