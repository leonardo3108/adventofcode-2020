numbers = []
for linha in open('input-10.txt'):
    numbers.append(int(linha.strip()))

ordered = sorted(numbers)
min = ordered[0]
max = ordered[-1]
print()
print('min output:       ', min)
print('max output:       ', max)
print('joltage of device:', max + 3)

last = 0
seq_diffs = []
for number in ordered:
    seq_diffs.append(number - last)
    last = number
seq_diffs.append(3)

diffs = {1:0, 3:0}
for diff in seq_diffs:
    diffs[diff] += 1
    
print('diffs:', diffs, diffs[1] * diffs[3])    

#o que vale sao as sequencias de 1
#os saltos de 3 sao de percorrimento obrigatorio, mas de 1 eh possivel pular

#mas se ha um salto de 1 isolado, soh ha essa possibilidade
#as sequencias de 2, 3 ou 4 saltos de 1 eh que permitem arranjos distintos
#2 saltos de 1: sao tres numeros em sequencia ex 3,4,5 - o que se pode fazer eh pular o do meio ou nao (2 possibilidades)
#3 saltos de 1: sao quatro numeros em sequencia ex 3,4,5,6 - o que se pode fazer eh pular ou nao cada um os do meio - 4 e 5 - gera 4 possibilidades
#4 saltos de 1: sao cinco numeros em sequencia ex 3,4,5,6,7 - o que se poderia fazer eh pular ou nao cada um os do meio - 4, 5 e 6 - seriam 8 possibilidades
#                                                             porem 3 e 7 estao distantes 4 jolts, nao pode! tem que usar pelo menos um dos 3 do meio, portanto sao 7 possibilidades

#Entao, parte-se de 1 possibilidade original (contar todos), dai para cada ocorrencia de sequencias de 2 a 4 mais saltos de 1  (nao ha 5 saltos em sequencia), multiplica-se o numero de possibilidades


print(seq_diffs)
rep = 0
choices = 1
for diff in seq_diffs:
    if diff == 1:
        rep += 1
    else:
        if rep == 2:
            choices *= 2
        elif rep == 3:
            choices *= 4
        elif rep == 4:
            choices *= 7
        rep = 0
print(choices)

#47552535724032