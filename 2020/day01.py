numeros = []
for linha in open('input-01.txt'):
    numeros.append(int(linha.strip()))

for numero in numeros:
    if 2020-numero in numeros:
        print(numero, 2020-numero, numero * (2020-numero))
        break
        
for numero1 in numeros:
    for numero2 in numeros:
        if numero1 < numero2:
            numero3 = 2020 - numero1 - numero2
            if numero3 in numeros and numero3 > numero2:
                print(numero1, numero2, numero3, numero1 * numero2 * numero3)

        