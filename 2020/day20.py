from math import sqrt

number = 0
tiles = {}
for line in [x.strip() for x in open('input-20.txt')]:
    if 'Tile' in line:
        number = int(line[5:9])
        tiles[number] = []
    elif line:
        tiles[number].append(line)

#print(', '.join([str(number) for number in sorted(tiles.keys())]))

borders = {}
tile_borders = {}

def append(border, number):
    if border in borders:
        borders[border].append(number)
    else:
        borders[border] = [number]

def get_borders(number):
    up = tiles[number][0]
    down = tiles[number][-1]
    left = right = ''
    for line in tiles[number]:
        left += line[0]
        right += line[-1]
    tile_borders[number] = {'up': up, 'down': down, 'left': left, 'right': right}
    return right, up, left, down

for number in tiles.keys():
    #print(number, tiles[number])
    right, up, left, down = get_borders(number)
    #print(number, 'up:', up, 'down:', down, 'left:', left, 'right:', right)
    append(up, number)
    append(down, number)
    append(left, number)
    append(right, number)

edges = []
corners = []
result = 1
for border in list(borders.keys()).copy():
    if len(borders[border]) == 1:
        number = borders[border][0]
        reverse = border[::-1]
        if reverse in borders:
            borders[reverse].append(-number)
        else:
            if number in edges:
                corners.append(number)
                result *= number
            else:
                edges.append(number)

print(' * '.join([str(corner) for corner in corners]), '=', result)

def flip_horizontal(number):
    flipped = []
    for line in tiles[number]:
        flipped.append(line[::-1])
    tiles[number] = flipped
    get_borders(number)

def flip_vertical(number):
    tiles[number] = list(reversed(tiles[number]))
    get_borders(number)

def rotate_clockwise(number):
    size = len(tiles[number])
    rotated = []
    for i in range(size):
        new_line = ''
        for line in tiles[number]:
            new_line += line[i]
        rotated.append(new_line)
    tiles[number] = rotated
    get_borders(number)
    
def check_border(f, border, cell, direction):
    if f:
        return f
    if border == tile_borders[cell][direction] or border == tile_borders[cell][direction][::-1]:
        return direction
    return ''

def find_border(border, cell):
    f = check_border('', border, cell, 'right')
    f = check_border(f, border, cell, 'left')
    f = check_border(f, border, cell, 'up')
    f = check_border(f, border, cell, 'down')
    return f

def find_neighbor(number, border):
    cell = 0
    original = border
    if border in borders.keys() and len(borders[border]) == 2:
        cell = [l for l in borders[border] if l != number][0]
    else:
        border = border[::-1]
        if border in borders.keys() and len(borders[border]) == 2:
            cell = [l for l in borders[border] if l != number][0]
    if cell == 0:
        print('neighbors:', borders[original])
        print('neighbors-r:', borders[original[::-1]])
    if cell < 0:
        cell = -cell
    return cell

directions = ['right', 'up', 'left', 'down']
turns = {'right':0, 'up':1, 'left':2, 'down':3}

def find_match(base, direction):
    oposite_direction = directions[(turns[direction] + 2) % 4]
    #print('-------------------------------------------')
    #print('x:', x, 'y:', y, 'direction:', direction)
    border = tile_borders[base][direction]
    cell = find_neighbor(base, border)
    #print('base:', base, direction + ':', border)
    face = find_border(border, cell)
    if y == 0 and x == 3:
        print(x, y, '0>', direction + ':', border, face + ':', tile_borders[cell][face], 'reverse:', tile_borders[cell][face][::-1])
        print(tile_borders[cell])
    #print('next:', cell, face + ':', tile_borders[cell][face])
    if face == direction:
        if direction in ['left', 'right']:
            flip_horizontal(cell)
        elif direction in ['up', 'down']:
            flip_vertical(cell)
    elif face != oposite_direction:
        rotate_clockwise(cell)
        face = directions[(turns[face] - 1) % 4]
        if y == 0 and x == 3:
            print(x, y, '1>', direction + ':', border, face + ':', tile_borders[cell][face], 'reverse:', tile_borders[cell][face][::-1])
            print(tile_borders[cell])
        if face == direction:
            if direction in ['left', 'right']:
                flip_horizontal(cell)
            elif direction in ['up', 'down']:
                flip_vertical(cell)
        if y == 0 and x == 3:
            print(x, y, '2>', direction + ':', border, face + ':', tile_borders[cell][face], 'reverse:', tile_borders[cell][face][::-1])
    if border == tile_borders[cell][oposite_direction][::-1]:
        if direction in ['left', 'right']:
            flip_vertical(cell)
        elif direction in ['up', 'down']:
            flip_horizontal(cell)
    if y == 0 and x == 3:
        print(x, y, '<<', direction + ':', border, oposite_direction + ':', tile_borders[cell][oposite_direction], 'reverse:', tile_borders[cell][oposite_direction][::-1])
    if border != tile_borders[cell][oposite_direction]:
        print('ERROR!  x =', str(x) + ', y =', y)
        print('borders:', tile_borders[cell])
        print('base:', base, direction + ':', border)
        print('next:', cell, oposite_direction + ':', tile_borders[cell][oposite_direction], face)
        exit()
    return cell

size = int(sqrt(len(tiles.keys())))
grid = [[0] * size for _ in range(size)]
for number in corners:
    if len(borders[tile_borders[number]['up']]) == 1:
        y = 0
    elif len(borders[tile_borders[number]['down']]) == 1:
        y = size-1
    if len(borders[tile_borders[number]['left']]) == 1:
        x = 0
    elif len(borders[tile_borders[number]['right']]) == 1:
        x = size-1
    grid[y][x] = number

for y in range(0, size):
    for x in range(0, size):
        if y == 0 and x > 0:
            cell = grid[0][x-1]
            direction = 'right'
        elif y > 0 and y < size - 1 or y == size - 1 and x > 0 and x < size - 1:
            cell = grid[y-1][x]
            direction = 'down'
        else:
            continue
        cell = find_match(cell, direction)
        if grid[y][x]:
            if grid[y][x] != cell:
                print('ERROR!', 'grid[' + str(y) + '][' + str(x) + ']', '=', grid[y][x], 'x', cell)
                exit()
        else:
            grid[y][x] = cell
    print(grid[y])

def show_tile(numbers):
    for i in range(len(tiles[numbers[0]][0])):
        print(' '.join([tiles[number][i] for number in numbers]))

for y in range(0, 2):
    print()
    show_tile([grid[y][x] for x in range(0, 12)])


