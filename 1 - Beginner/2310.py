# URI Online Judge 2310

N = int(input())
S, B, A = 0, 0, 0
s, b, a = 0, 0, 0

for jogador in range(N):
    nome = input()
    
    tentativas = input().split()
    S += int(tentativas[0])
    B += int(tentativas[1])
    A += int(tentativas[2])
    
    sucessos = input().split()
    s += int(sucessos[0])
    b += int(sucessos[1])
    a += int(sucessos[2])
    
print('Pontos de Saque: {:.2f} %.'.format( (s/S) * 100))
print('Pontos de Bloqueio: {:.2f} %.'.format( (b/B) * 100))
print('Pontos de Ataque: {:.2f} %.'.format( (a/A) * 100))