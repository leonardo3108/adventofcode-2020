earliest, second = open('input-13.txt')
earliest = int(earliest.strip())
ids = [int(id) for id in second.strip().replace('x,', '').split(',')]
print('earliest:', earliest)
print('ids:', ids)
waits = [id - earliest % id for id in ids]
loops = [earliest // id for id in ids]
print('waits:', waits)
print('loops:', loops)
timestamps = []
for i, id in enumerate(ids):
    timestamps.append(loops[i] * id + id)
print('timestamps:', timestamps)
min_wait = min(waits)
first = ids[waits.index(min_wait)]
print('answer:', min_wait, '*', first, '=', min_wait * first)
print()

print('All ids:')
all_ids = [int(id) for id in second.strip().replace('x,', '0,').split(',')]
print(all_ids)
print()

def strf(v):
    if v >= 0:
        return str(v)
    return '(' + str(v) + ')'

def strt(v):
    if v >= 0:
        return '+ ' + str(v)
    return '- ' + str(-v)

key = ids[0]
for k, id in enumerate(ids):
    if k == 0:
        a = ids[k]
        c1 = all_ids.index(id)
    elif k < 1000:
        b = ids[k]
        c2 = all_ids.index(id)
        if b > a:
            a, b, c1, c2 = b, a, c2, c1
        print('a:', a, '  c1:', c1, '  b:', b, '  c2:', c2)
        print('\tEquacao diofantina bruta:', str(a) + 'x -', c1, '=', str(b) + 'y -', c2, '   (ax - c1 = by - c2)')
        c = abs(c2 - c1)
        if c2 > c1:
            print('\tEquacao diofantina limpa:', str(b) + 'y +', str(a) + '(-x) =', c, '   (ax + by = c)')
        else:
            print('\tEquacao diofantina limpa:', str(a) + 'x +', str(b) + '(-y) =', c, '   (ax + by = c)')
        restos = [a]
        q = []
        r = b
        while r != 0:
            restos.append(r)
            r = restos[-2] % restos[-1]
            q.append(restos[-2] // restos[-1])            
        d = restos[-1]
        print('\td = mdc(' + str(a) + ',' + str(b) + ') =', d, ' (algoritmo de euclides - restos:', str(restos) + ', quocientes:', str(q) + ')')
        if c % d != 0:
            print('Erro: equacao diofantina nao admite solucao pois', c, 'nao eh divisivel por', d)
            break
        print('\tEquacao diofantina admite solucao pois', c, 'eh divisivel por', d)
        print('\tRelacao de Bizout:', d, '=', str(a) + 's +', str(b) + 't  (mdc(a,b) = as + bt)')
        ts = [0, 1]
        for i in range(len(q)-2,-1,-1):
            ts.append(ts[-2] + ts[-1] * q[i])
            #print('\t\t', q[i], ts[-2], ts)
        if len(q) % 2 == 0:
            s, t = ts[-2], -ts[-1]
        else:
            s, t = -ts[-2], ts[-1]
        print('\ts =', str(s) + ', t =', t, ' ==>  as + bt =', str(a) + '.' + strf(s), '+', str(b) + '.' + strf(t), '=', str(a*s), strt(b*t), '= 1')
        if c2 > c1:
            x0 = -c*s
            y0 = c*t
            print('\t-x0 = c.s =', str(c) + '.' + strf(s), '=', -x0, ' ==>  x0 =', x0)
            print('\ty0 = c.t =', str(c) + '.' + strf(t), '=', y0)
            print('\tSubstituindo na equacao diofantina:   ax + by =', str(a) + '(-x) +', str(b) + 'y =', a*x0, strt(-b*y0), '=', -a*x0 + b*y0, '= c')
        else:
            x0 = c*s
            y0 = -c*t
            print('\tx0 = c.s =', str(c) + '.' + strf(s), '=', x0)
            print('\t-y0 = c.t =', str(c) + '.' + strf(t), '=', -y0, ' ==>  y0 =', y0)
            print('\tSubstituindo na equacao diofantina:   ax + by =', str(a) + 'x +', str(b) + '(-y) =', a*x0, strt(-b*y0), '=', a*x0 - b*y0, '= c')
        R0 = a * x0 - c1
        k = -(R0 // (a * b))
        print('\tTodas solucoes da diofantina: x = x0 + bk, y = y0 - ak, k inteiro. Melhor solucao (earliest) para k =', str(k), '(R0=' + str(R0) + ', ab=' + str(a*b) + '):')
        x = x0 + b * k
        y = y0 + a * k
        earliest = R0 + k * a * b
        print('\t\tx =', x0, '+', str(b) + '.' + strf(k), '=', x0, strt(b*k), '=', x)
        print('\t\tearliest = a * x - c1 =', a, '*', x, '-', c1, '=', a*x, '-', c1, '=', earliest)
        a, c1 = earliest, 0
    else:
        break
print('final earliest = ', earliest)

exit()
key = ids[0]
for k, id in enumerate(ids):
    offset = all_ids.index(id)
    diff = abs(id - key)
    print('id:', str(id).rjust(3), '  offset:', str(offset).rjust(2), ' key:', key, '  diff:', str(diff).rjust(3))
    if k == 1:
        loop = [(i * id) % key for i in range(1, key+1)].index(offset) + 1
        earliest = loop * id - offset
        old_key = key
        key = id * key
        print('\tloops:', loop, ' timestamp:', loop * id, ' earliest:', earliest, ' loops:', earliest // old_key, ' dist:', key, ' next:', key + earliest)
    if k == 2:
        for i in range(1, key+1):
            print('\t', i, i*id, i*id % key)
            break
#        print([(i * id) for i in range(1, key+1)])
 #       loop = [(i * id) % key for i in range(1, key+1)].index(offset) + 1
  #      print(loop* id)
    if k > 1:
        break


