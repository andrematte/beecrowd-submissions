# URI Online Judge 1179

N = 15
par = []
impar = []

def limpa_vetor(vetor, tipo):
    for i in range(len(vetor)):
        print(tipo + '[{}] = {}'.format(i, vetor[i]))
    return []
        
for i in range(15):
    entrada = int(input())
    
    if entrada % 2 == 0:
        par.append(entrada)
    else:
        impar.append(entrada)
        
    if len(par) == 5:
        par = limpa_vetor(par, 'par')
    
    if len(impar) == 5:
        impar = limpa_vetor(impar, 'impar')
        
limpa_vetor(impar, 'impar')
limpa_vetor(par, 'par')