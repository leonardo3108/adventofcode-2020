instructions = []

for linha in open('input-12.txt'):
    instruction = linha.strip()
    instructions.append((instruction[0], int(instruction[1:])))

#print(instructions)
directions = ['E', 'N', 'W', 'S']
change = {'L': 1, 'R':-1}

#instructions = [('F', 10), ('N', 3), ('F', 7), ('R', 90), ('F', 11)]

def show(action, value, facing, position_east, position_north, waypoint_east, waypoint_north):
    text = 'east: ' + str(position_east).rjust(6) + '  north: ' +  str(position_north).rjust(6)
    if facing:
        text = 'facing: ' + facing + '   ' + text
    text = '    -->     ' + text
    if waypoint_east or waypoint_north:
        text += '        waypont east: ' + str(waypoint_east).rjust(3) + '  waypont north: ' +  str(waypoint_north).rjust(3)
    if action:
        print ('action:', action, ' value:', str(value).rjust(3), text)
    else:
        print ('Initial    settup    ', text)

facing, position_east, position_north = 'E', 0, 0
#show(None, 0, facing, position_east, position_north, 0, 0)

for i, (action, value) in enumerate(instructions):
    if action in ('L','R'):
        turn = change[action] * value // 90
        facing = directions[(directions.index(facing) + turn) % 4]
    else:
        if action == 'F':
            move = facing
        else:
            move = action
        if   move == 'N':
            position_north += value
        elif move == 'S':
            position_north -= value
        elif move == 'E':
            position_east  += value
        elif move == 'W':
            position_east  -= value
    #show(action, value, facing, position_east, position_north, 0, 0)
    #if i == 10:
    #    break
print('manhattan distance: ', abs(position_east) + abs(position_north))
print()

position_east, position_north, waypoint_east, waypoint_north = 0, 0, 10, 1
#show(None, 0, None, position_east, position_north, waypoint_east, waypoint_north)

for i, (action, value) in enumerate(instructions):
    if action in ('L','R'):
        turn = change[action] * value // 90 % 4
        if turn == 1 or turn == 3:
            swap = waypoint_east
            waypoint_east  = -waypoint_north
            waypoint_north = swap
        if turn == 2 or turn == 3:
            waypoint_east  = -waypoint_east
            waypoint_north = -waypoint_north
    else:
        if   action == 'N':
            waypoint_north += value
        elif action == 'S':
            waypoint_north -= value
        elif action == 'E':
            waypoint_east  += value
        elif action == 'W':
            waypoint_east  -= value
        if action == 'F':
            position_north += waypoint_north * value
            position_east  += waypoint_east * value
    #show(action, value, None, position_east, position_north, waypoint_east, waypoint_north)
    if i == 1000:
        break
print('manhattan distance: ', abs(position_east) + abs(position_north))



