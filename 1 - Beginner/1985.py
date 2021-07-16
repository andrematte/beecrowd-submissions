# URI Online Judge 1985

produtos = {
    '1001': 1.5,
    '1002': 2.5,
    '1003': 3.5,
    '1004': 4.5,
    '1005': 5.5
}

N = int(input())
soma = 0

for n in range(N):
    entrada = input().split()
    produto = entrada[0]
    quantidade = float(entrada[1])
    
    soma += quantidade * produtos[produto]
    
print('{:.2f}'.format(soma))