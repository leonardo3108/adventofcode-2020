qtd_valids = 0
for linha in open('input-02.txt'):
    campos = linha.strip().split(':')
    qtd, let = campos[0].split(' ')
    min_qtd, max_qtd = qtd.split('-')
    pwd = campos[1].strip()
    qtd = 0
    for l in pwd:
        if l == let:
            qtd += 1
    vality = qtd >= int(min_qtd) and qtd <= int(max_qtd)
    qtd_valids += vality
    print(min_qtd, max_qtd, let, pwd, qtd, vality)
print(qtd_valids)

qtd_valids = 0
for linha in open('input-02.txt'):
    campos = linha.strip().split(':')
    qtd, let = campos[0].split(' ')
    min_pos, max_pos = qtd.split('-')
    pwd = campos[1].strip()
    qtd = 0
    l1 = pwd[int(min_pos)-1]
    l2 = pwd[int(max_pos)-1]
    vality = (let == l1) ^ (let == l2)
    qtd_valids += vality
    print(min_pos, max_pos, let, pwd, l1, l2, vality)
print(qtd_valids)
