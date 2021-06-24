# URI Online Judge 1150

# %%
X = int(input())
Z = int(input())

soma = X
contador = 0

while Z <= X:
    Z = int(input())
    
while soma <= Z:
    contador = contador + 1
    soma += X + 1*contador
    
    #print(f'soma: {soma},    contador: {contador}')

contador = contador + 1
print(contador)
