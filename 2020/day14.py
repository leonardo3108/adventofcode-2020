memory = {}

def apply_mask(value, mask, address, showing, type):
    if showing:
        print('mem-' + str(address) + ':')
    v = value
    a = address
    str_v = str_a = str_result = ''
    result = 0
    relative = 1
    for bit in range(0,36):
        vv = v % 2
        aa = a % 2
        str_v = str(vv) + str_v
        str_a = str(aa) + str_a
        m = mask[-1-bit]
        if type == 'value':
            if m == 'X':
                str_result = str(vv) + str_result
                result += vv * relative
            else:
                str_result = m + str_result
                result += int(m) * relative
        elif type == 'address':
            if m == '0':
                str_result = str(aa) + str_result
                result += aa * relative
            else:
                str_result = m + str_result
        v = v // 2
        a = a // 2
        relative *= 2
    if type == 'address':
        addresses = [str_result]
        for bit in range(0,36):
            m = str_result[-1-bit]
            if m == 'X':
                #print(bit, 'addresses:', len(addresses))
                new_addresses = []
                for a in addresses:
                    if a[-1-bit] == 'X':
                        a0 = '0'
                        a1 = '1'
                        if bit < 35:
                            a0 = a[:-1-bit] + a0
                            a1 = a[:-1-bit] + a1
                        if bit > 0:
                            a0 += a[-bit:]
                            a1 += a[-bit:]
                        new_addresses.append(a0)
                        new_addresses.append(a1)
                addresses = new_addresses
        result = []
        for a in addresses:
            r = 0
            for b in a:
                r = r*2 + int(b)
            result.append(r)
            memory[r] = value
    if showing:
        if type == 'value':
            print('\tvalue  ', str_v, '(' + str(value) + ')')
        elif type == 'address':
            print('\taddress', str_a, '(' + str(address) + ')')
        print('\tmask   ', mask)
        print('\tresult ', str_result, '(' + str(result) + ')')
    if type == 'value':
        memory[address] = result
    return result

def process(entrada, showing, type):
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
                apply_mask(value, mask, address, showing, type)
            else:
                print(variavel + str(':'), value, '=================')
                break
    sum = 0
    #print('\nMemory content:')
    for address in memory.keys():
        sum += memory[address]
        #print('\t' + str(address) + ':', memory[address])
    print('\nsum:', sum)
    
process(open('input-14.txt'), False, 'value')

process(['mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 'mem[8] = 11', 'mem[7] = 101', 'mem[8] = 0'], True, 'value')

#process(['mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 'mem[8] = 11', 'mem[7] = 101', 'mem[8] = 0'], True, 'address')

process(open('input-14.txt'), True, 'address')
