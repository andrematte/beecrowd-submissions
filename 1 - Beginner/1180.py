# URI Online Judge 1180

N = int(input())
X = [int(item) for item in input().split()]

print('Menor valor: {}'.format(min(X)))
print('Posicao: {}'.format(X.index(min(X))))