# URI Online Judge 2702

disponiveis = [int(i) for i in input().split()]
desejadas = [int(i) for i in input().split()]

falta = 0


for disp, desej in zip(disponiveis, desejadas):
    if desej > disp:
        falta += desej - disp
        
print(falta)