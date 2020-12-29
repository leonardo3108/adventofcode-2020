input = open('input-24.txt')

input = ['sesenwnenenewseeswwswswwnenewsewsw', 'neeenesenwnwwswnenewnwwsewnenwseswesw', 'seswneswswsenwwnwse', 'nwnwneseeswswnenewneswwnewseswneseene', 'swweswneswnenwsewnwneneseenw', 'eesenwseswswnenwswnwnwsewwnwsene', 'sewnenenenesenwsewnenwwwse', 'wenwwweseeeweswwwnwwe', 'wsweesenenewnwwnwsenewsenwwsesesenwne', 'neeswseenwwswnwswswnw', 'nenwswwsewswnenenewsenwsenwnesesenew','enewnwewneswsewnwswenweswnenwsenwsw', 'sweneswneswneneenwnewenewwneswswnese', 'swwesenesewenwneswnwwneseswwne', 'enesenwswwswneneswsenwnewswseenwsese', 'wnwnesenesenenwwnenwsewesewsesesew', 'nenewswnwewswnenesenwnesewesw', 'eneswnwswnwsenenwnwnwwseeswneewsenese', 'neswnwewnwnwseenwseesewsenwsweewe', 'wseweeenwnesenwwwswnew']

paths = []
for line in input:
    size = len(line.rstrip())
    pos = 0
    path = {'e': 0, 'w': 0, 'se': 0, 'sw': 0, 'ne': 0, 'nw': 0}
    while pos < size:
        if line[pos] in 'ew':
            path[line[pos]] += 1
            pos += 1
        else:
            path[line[pos:pos+2]] += 1
            pos += 2
    paths.append(path)

#print(paths)

flips = []
for path in paths:
    e = path['e'] - path['w']
    ne = path['ne'] - path['sw']
    nw = path['nw'] - path['se']
    nw += ne
    e += ne
    flips.append({'e': e, 'nw': nw})
    
#print(flips)

tile = {}

def str_position(e, nw):
    return str(e) + ';' + str(nw)

def complete(e, nw):
    position = str_position(e, nw)
    if position not in tile.keys():
        tile[position] = 0

def is_black(e, nw):
    position = str_position(e, nw)
    return position in tile.keys() and tile[position]

def do_flip(e, nw):
    position = str_position(e, nw)
    if position in tile.keys():
        tile[position] = 1 - tile[position]
    else:
        tile[position] = 1

def do_flips(flips):
    for flip in flips:
        do_flip(flip['e'], flip['nw'])

def change():
    for position in list(tile.keys()).copy():
        e, nw = [int(x) for x in position.split(';')]
        if tile[position]:
            complete(e+1, nw  )
            complete(e-1, nw  )
            complete(e+1, nw+1)
            complete(e  , nw+1)
            complete(e+1, nw-1)
            complete(e  , nw-1)
    print(tile)
    flips = []
    for position in tile.keys():
        e, nw = [int(x) for x in position.split(';')]
        black = tile[position]
        blacks = 0
        blacks += is_black(e+1, nw  )
        blacks += is_black(e-1, nw  )
        blacks += is_black(e+1, nw+1)
        blacks += is_black(e  , nw+1)
        blacks += is_black(e+1, nw-1)
        blacks += is_black(e  , nw-1)
        #Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
        #Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
        if black and blacks != 1 and blacks != 2 or not black and blacks == 2:
            flips.append({'e': e, 'nw': nw})
            print('(' + position + ')=' + str(black), 'x', str(blacks))
    do_flips(flips)
    
do_flips(flips)

#print(tile)

def blacks():
    result = 0
    for position in tile.keys():
        result += tile[position]
    return result

day = 0
print('Day', day, '-', blacks())
change()
print('Day', day, '-', blacks())
print(tile)





