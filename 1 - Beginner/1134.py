# URI Online Judge 1134
Codigo = 0
Alcool, Gasolina, Diesel = 0, 0, 0

while Codigo != 4:
    Codigo = int(input())

    if Codigo == 1:
        Alcool += 1
    elif Codigo == 2:
        Gasolina += 1
    elif Codigo == 3:
        Diesel += 1

print("MUITO OBRIGADO")
print("Alcool: {}".format(Alcool))
print("Gasolina: {}".format(Gasolina))
print("Diesel: {}".format(Diesel))