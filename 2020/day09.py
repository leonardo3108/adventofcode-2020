numbers = []
for linha in open('input-09.txt'):
    numbers.append(int(linha.strip()))
    
#print(numbers)

for i, number in enumerate(numbers[25:]):
    possibilities = numbers[i:i+25]
    found = False
    for element in possibilities:
        if number - element in possibilities:
            found = True
            break
    if found:
        pass
        #print(str(i) + ':', number, '=', element, '+', number - element)
    else:
        print('first key (' + str(i) + '):', number)
        break

for i, element_i in enumerate(numbers):
    sum = element_i
    smallest = largest = element_i
    for j, element_j in enumerate(numbers[i+1:]):
        sum += element_j
        if element_j > largest:
            largest = element_j
        elif element_j < smallest:
            smallest = element_j
        if sum >= number:
            break
    if sum == number:
        break

print('\nrange:', element_i, '+', element_j, '=', sum)
print('\nsecond key:', smallest, '+', largest, '=', smallest + largest)