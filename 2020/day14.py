memory = {}

def apply_mask(value, mask, address, showing):
    if showing:
        print('mem-' + str(address) + ':')
    v = value
    str_v = str_result = ''
    result = 0
    relative = 1
    for bit in range(0,36):
        vv = v % 2
        str_v = str(vv) + str_v
        m = mask[-1-bit]
        if m == 'X':
            str_result = str(vv) + str_result
            result += vv * relative
        else:
            str_result = m + str_result
            result += int(m) * relative
        v = v // 2
        relative *= 2
    if showing:
        print('\tvalue ', str_v, '(' + str(value) + ')')
        print('\tmask  ', mask)
        print('\tresult', str_result, '(' + str(result) + ')')
    memory[address] = result
    return result

def process(entrada, showing):
    for linha in entrada:
        campos = linha.split('=')
        variavel, value = campos[0].strip(), campos[1].strip()
        if variavel == 'mask':
            mask = value
            #print('mask:', mask)
        else:
            if variavel[:4] == 'mem[':
                address = int(variavel[4:-1])
                variavel = 'mem'
                value = int(value)
                apply_mask(value, mask, address, showing)
            else:
                print(variavel + str(':'), value, '=================')
                break
    sum = 0
    #print('\nMemory content:')
    for address in memory.keys():
        sum += memory[address]
        #print('\t' + str(address) + ':', memory[address])
    print('\nsum:', sum)
    
process(open('input-14.txt'), False)

process(['mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 'mem[8] = 11', 'mem[7] = 101', 'mem[8] = 0'], True)

