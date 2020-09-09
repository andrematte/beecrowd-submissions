# URI Online Judge 1149

Entrada = input()

Entrada = list(map(int, Entrada.split()))

A = Entrada[0]
A_copy = A
sum = 0

for i in Entrada[1:]:
    if i > 0:
        N = i

for j in range(0,N):
    sum += A_copy + j

print(sum)