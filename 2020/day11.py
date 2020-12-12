seats = []

def print_seats(seats):
    print()
    for l in seats:
        print (l)
        
for linha in open('input-11.txt'):
    seats.append(linha.strip())
#print_seats(seats)
W = len(seats[0])
H = len(seats)

def find_ocupied(seats, H, W, y, x, sy, sx, first):
    dx = sx
    dy = sy
    while True:
        if y + dy < 0 or y + dy >= H or x + dx < 0 or x + dx >= W:
            return False
        if seats[y+dy][x+dx] == '#':
            return True
        if seats[y+dy][x+dx] == 'L':
            return False
        if first:
            return False
        dx += sx
        dy += sy

def count_visible(seats, H, W, y, x, first, limit):
    count = 0
    for dx in range(-1, +2):
        for dy in range(-1, +2):
            if (dx != 0 or dy != 0) and find_ocupied(seats, H, W, y, x, dy, dx, first):
                count += 1
                if count >= limit:
                    return False
    return True
    
def process(seats, limit, first):
    new_seats = []
    changes = 0
    for i in range(H):
        new_line = ''
        for j in range(W):
            #If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
            if seats[i][j] == 'L':
                if count_visible(seats, H, W, i, j, first, 1):
                    new_line += '#'
                    changes += 1
                else:
                    new_line += 'L'
            #If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
            elif seats[i][j] == '#':
                if count_visible(seats, H, W, i, j, first, limit):
                    new_line += '#'
                else:
                    new_line += 'L'
                    changes += 1
            #Otherwise, the seat's state does not change.
            else:
                new_line += seats[i][j]
        new_seats.append(new_line)
    return new_seats, changes

def count_ocupied(seats):
    count = 0
    for i in range(H):
        for j in range(W):
            if seats[i][j] == '#':
                count += 1
    print(count)

g = 0    
changes = -1
while changes:
    g += 1
    #seats, changes = process(seats, 4, True)
    seats, changes = process(seats, 5, False)
    #print_seats(seats)
    print(g, changes)

#print_seats(seats)
count_ocupied(seats)
