# URI Online Judge 2753

numeros = [97+i for i in range(0,26)]
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
          'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']

for numero, letra in zip(numeros, letras):
    print('{} e {}'.format(numero, letra))
