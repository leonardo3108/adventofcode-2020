def execute(numbers, limit, goal):
    spoken_numbers = {}
    
    def spoken(last, turn):
        if last in spoken_numbers:
            retorno = turn - spoken_numbers[last][-1]
            #print(turn, '-', spoken_numbers[last][-1])
            spoken_numbers[last].append(turn)
            return retorno
        else:
            spoken_numbers[last] = [turn]
            return 0
    
    #print(numbers)
    for i, n in enumerate(numbers[:-1]):
        spoken(n, i+1)
    #print(spoken_numbers)

    last = numbers[-1]
    for turn in range(len(numbers), limit):
        #print()
        texto = 'turn: ' + str(turn) + '  last: ' + str(last)
        #print('\n', spoken_numbers)
        last = spoken(last, turn)
        #print(texto, ' speak:', last)
    if goal == last:
        result = 'ok'
    elif goal:
        result = 'nok'
    else:
        result = ''
    print(numbers, str(limit)+':', last, result)
 
execute([0, 3, 6], 10, 0)
execute([1,3,2], 2020, 1)
execute([2,1,3], 2020, 10)
execute([1,2,3], 2020, 27)
execute([2,3,1], 2020, 78)
execute([3,2,1], 2020, 438)
execute([3,1,2], 2020, 1836)
execute([2, 0, 6, 12, 1, 3], 2020, None)
execute([2, 0, 6, 12, 1, 3], 30000000, None)

