map = list()
for linha in open('input-03.txt'):
    map.append(linha.strip())

def route(dx, dy, show):
    x = y = 0
    ly = len(map)
    trees = 0
    strees = '  0'
    while y < ly and y >= 0:
        field = map[y]
        lx = len(field)
        px = x%lx
        if map[y][px] == '#':
            field = field[:px] + 'X' + field[px+1:]
            trees += 1
            strees = str(trees).rjust(3)
        else:
            field = field[:px] + 'O' + field[px+1:]
            strees = '   '
        if show:
            print(map[y], field, str(x).rjust(3), str(y).rjust(3), map[y][px], strees)
        x += dx
        if dy > 1 and show:
            for l in range(y+1, y+dy):
                if l >= ly:
                    break
                print(map[l], map[l], '   ', str(l).rjust(3))
        y += dy
    if show:
        print()
    print('Result:', dy, dx, trees)
    return trees

mult = 1
mult *= route(1, 1, False)
mult *= route(3, 1, False)
mult *= route(5, 1, False)
mult *= route(7, 1, False)
mult *= route(1, 2, False)
print('Final result', mult)
