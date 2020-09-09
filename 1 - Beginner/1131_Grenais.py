# URI Online Judge 1131

grenais=0
inter=0
gremio=0
empates=0
cont=0
x,y = map(int, input().split())
while True:
    if x>y:
        inter+=1
        grenais+=1
    elif y>x:
        gremio+=1
        grenais+=1
    elif x==y:
        empates+=1
        grenais+=1

    n=int(input("Novo grenal (1-sim 2-nao)\n"))
    cont+=1
    if n == 2:
        break
    elif n == 1:
        x,y = map(int, input().split())

print("{} grenais".format(grenais))
print("Inter:{}".format(inter))
print("Gremio:{}".format(gremio))
print("Empates:{}".format(empates))
if inter > gremio:
    print("Inter venceu mais")
elif gremio > inter:
    print("Gremio venceu mais")
elif gremio == inter:
    print("Nao houve vencedor")