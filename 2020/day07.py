rules = {}
for linha in open('input-07.txt'):
    palavra = linha.strip().split()
    color = ' '.join(palavra[0:2])
    subs = []
    if palavra[4] == 'no':
        qtde = 0
    else:
        qtde = int(palavra[4])
        for i in range(1, len(palavra) // 4):
            subs.append((int(palavra[i*4]), ' '.join(palavra[i*4+1:i*4+3])))
    rules[color] = {'quantidade': qtde, 'subs': subs}



def find_supers(sub, rules, total):
    supers = set()
    for color in rules.keys():
        for _, subc in rules[color]['subs']:
            if sub == subc:
                if color not in total:
                    supers.add(color)
    return supers
 
total = set()
findings = {'shiny gold'}
while findings:
    new_findings = set()
    for color in findings:
        last = find_supers(color, rules, total)
        #print(color, last)
        new_findings.update(last)
    total.update(new_findings)
    #print('\n', len(total), '==>', sorted(total), '\n')

    findings = new_findings


def find_subs(super, rules, nivel):
    retorno = 1
    if rules[super]['subs']:
        pass
        #print('\t' * (nivel - 1), super, 'contains')
    for subq, subc in rules[super]['subs']:
        #print('\t' * nivel, subq, subc)
        retorno += subq * find_subs(subc, rules, nivel + 1)
    #print('\t' * (nivel - 1), super, '=', retorno)
    return retorno

print(len(rules), len(total), find_subs('shiny gold', rules, 1) - 1)

