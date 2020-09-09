# URI Online Judge 1101
M, N, soma = 0, 0, 0

M, N = input().split(' ')
M, N = int(M), int(N)

if M < N:
    menor = M
    maior = N
else:
    menor = N
    maior = M

while M > 0 and N > 0:
    for c in range(menor, maior+1):
        soma += c
        print('{} ' .format(c), end="")
    print('Sum={}' .format(soma))
    soma = 0

    M, N = input().split(' ')
    M, N = int(M), int(N)

    if M < N:
        menor = M
        maior = N
    else:
        menor = N
        maior = M