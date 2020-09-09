# URI Online Judge 1094

N = int(input())

num_ratos = 0
num_sapos = 0
num_coelhos = 0

total = 0

for i in range(1,N+1):

    entrada = input()

    if entrada.split()[1] == 'C':
        num_coelhos += int(entrada.split()[0])
    elif entrada.split()[1] == 'S':
        num_sapos += int(entrada.split()[0])
    elif entrada.split()[1] == 'R':
        num_ratos += int(entrada.split()[0])

total = num_ratos + num_coelhos + num_sapos

print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(num_coelhos))
print("Total de ratos: {}".format(num_ratos))
print("Total de sapos: {}".format(num_sapos))
print("Percentual de coelhos: {0:.2f} %".format((100*num_coelhos/total)))
print("Percentual de ratos: {0:.2f} %".format((100*num_ratos/total)))
print("Percentual de sapos: {0:.2f} %".format((100*num_sapos/total)))