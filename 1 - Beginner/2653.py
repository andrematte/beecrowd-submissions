# URI Online Judge 2653

joias = {}

while True:
    try:
        entrada = input()
        
        try:
            joias[entrada] += 1
        except:
            joias[entrada] = 1
        
    except EOFError:
        break
    
print(len(joias.keys()))