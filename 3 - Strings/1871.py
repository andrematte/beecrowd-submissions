# URI Online Judge 1871

while True:
    entrada = [int(i) for i in input().split()]
    if entrada[0] == 0 and entrada[1] == 0:
        break
    
    soma = str(sum(entrada)).replace('0','')
    print(soma)