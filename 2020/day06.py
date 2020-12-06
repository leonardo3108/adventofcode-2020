groups = []
group = {}
for linha in open('input-06.txt'):
    linha = linha.strip()
    if linha:
        if 'forms' not in group:
            group['forms'] = []
        group['forms'].append(linha)
        for c in linha:
            if c in group:
                group[c] += 1
            else:
                group[c] = 1
    else:
        groups.append(group)
        group = {}
groups.append(group)

any = all = 0
for group in groups:
    #any += len(group.keys())-1
    forms = len(group['forms'])
    for c in group.keys():
        if c != 'forms':
            any += 1
            if group[c] == forms:
                all += 1
print(any, all)    