input = open('input-19.txt')
show = False
#input=['0: 4 1 5', '1: 2 3 | 3 2', '2: 4 4 | 5 5', '3: 4 5 | 5 4', '4: "a"', '5: "b"', '', 'ababbb', 'bababa', 'abbbab', 'aaabbb', 'aaaabbb']
show = True

status = 'rules'
messages = []
rule = {}
final_rule = {}
for linha in input:
    if linha.strip():
        if status == 'text':
            messages.append(linha.strip())
        else:
            id, body = linha.strip().split(':')
            if '"' in body:
                rule[id] = final_rule[id] = body.strip().strip('"')
            else:
                rule[id] = body.strip()
    else:
        status = 'text'

def multiplex(r, show):
    if show:
        print(r)
    # Fase 1 - mapping openings and closings    
    openings = [i for i, c in enumerate(r) if c == '(']
    r_openings = list(reversed(openings))
    closing = {}
    closings = []
    for opening in r_openings:
        pos = opening
        while opening not in closing.keys():
            pos = r.index(')', pos)
            if pos in closings:
                pos += 1
            else:
                closing[opening] = pos
                closings.append(pos)
    # Fase 2 - resolving crossings (double parenthesis expressions)
    last_opening = 999999
    x = []
    last_cross = 0
    before1 = r
    for opening in r_openings:
        if last_opening < 999999 and last_opening > closing[opening]:
            if '|' not in r[closing[opening]:last_opening]:
                x.append(r[last_opening:closing[last_opening]+1])
                str_x = 'x' + str(last_cross)
                #if show:
                #    print('\t ' + str_x + ' = "' + x[last_cross] + '"')
                before1 = before1[:last_opening] + str_x + before1[closing[last_opening]+1:]
                #if show:
                #    print('\t before1 = "' + before1 + '"')
                last_cross += 1
        last_opening = opening
    if x:
        after1 = multiplex(before1, False)
        #if show:
        #    print('\t after1 = "' + after1 + '"')
        before2 = after1
        for i, xi in enumerate(x):
            before2 = before2.replace('x' + str(i), xi)
        #if show:
        #    print('\t before2 = "' + before2 + '"')
        after2 = multiplex(before2, False)
        if show:
            #print('\t after2 = "' + after2 + '"')
            print('\t', '"' + r + '"  >->  "' + before1 + '"  ##>  "' + after1 + '"  >->  "' + before2 + '"  ##>  "' + after2 + '"')
        return after2
    # Fase 3 - multiplexing (decoding parenthesis expressions)
    change = {}
    for opening in openings:
        inside = r[opening + 2 : closing[opening] - 1]
        left = r[: opening - 1]
        if opening == 0:
            left = ''
        elif '|' in left:
            #left = left[left.index('|') + 2:] first x last
            left = left[len(left) - left[::-1].index('|') + 1:]
        right = r[closing[opening] + 2:]
        if right and '|' == right[0]:
            right = ''
        elif '|' in right:
            right = right[:right.index('|') - 1]
        before = (left + ' ( ' + inside + ' ) ' + right).strip()
        if show:
            print('\t', left, '+', inside, '+', right)
        after = ' | '.join([(left + ' ' + p.strip() + ' ' + right).strip() for p in inside.split('|')])
        change[before] = after
        if show:
            print('\t\t', before, '->', after)
    for before in change.keys():
        r = r.replace(before, change[before])
    return r
    
def decode_text(r, show):
    if ' ' in r:
        s = [decode_text(p, show) for p in r.split()]
        return ' '.join(s)
    if r in rule.keys():
        return decode_rule(r, show)
    return r

def decode_rule(id, show):
    r = rule[id]
    if id in final_rule.keys():
        if r != final_rule[id] and show:
            print(str(id) + ':', '"' + r + '" ==> "' + final_rule[id] + '"')
    else:
        if show:
            print(str(id) + ':', '"' + r + '"')
        if '|' in r:
            s = [decode_text(p.strip(), show) for p in r.split('|')]
            f = ' | '.join(s)
            if '(' in f:
                ff = multiplex(f, False)
                if show:
                    print(f, '##>', ff)
                f = ff
            final_rule[id] = '( ' + f + ' )'
        else:
            f = decode_text(r.strip(), show)
            if '(' in f:
                ff = multiplex(f, False)
                if show:
                    print(f, '##>', ff)
                f = ff
            final_rule[id] = f
        if show:
            print(str(id) + ':', '"' + r + '" --> "' + final_rule[id] + '"')
    return final_rule[id]

if show:
    print('Decoding rules:')
    for id in final_rule.keys():
        print(str(id) + ':', final_rule[id])
else:
    print('Decoding rules...')

rules = [r.replace(' ', '') for r in decode_rule('0', show).split('|')]
uniques = []

if show:
    print('\nRules (final):')
for r in sorted(rules):
    if r not in uniques:
        uniques.append(r)
        if show:
            print(r)
if not show:
    print('Rules (final):', len(rules), ' Uniques:', len(uniques))
print('\nVerifying messages (' + str(len(messages)) + '):')
match = {}
for message in messages:
    for rule in rules:
        if message in rule:
            match[message] = rule
            if show:
                print('Message "' + message + '" matches rule "' + rule + '".')
            break
    if show and message not in match.keys():
        print('Message "' + message + '" does not match any rule."')
print()
print(len(match))
            