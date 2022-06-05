# Beecrowd 3302

N = int(input())
answers = []

for n in range(N):
    answer = int(input())
    answers.append(answer)

for n in range(N):
    print('resposta {}: {}'.format(n+1, answers[n]))
