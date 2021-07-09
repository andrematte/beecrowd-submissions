# URI Online Judge 2780

# Dada a distância D do robô até o início da quadra, onde está a cesta, a regra é a seguinte:
# • Se D ≤ 800, a cesta vale 1 ponto;
# • Se 800 < D ≤ 1400, a cesta vale 2 pontos;
# • Se 1400 < D ≤ 2000, a cesta vale 3 pontos.

N = int(input())

if N <= 800:
    print(1)
elif N >= 801 and N <= 1400:
    print(2)
elif N >= 1401 and N <= 2000:
    print(3)