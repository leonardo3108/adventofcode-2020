max_seat_id = 0
seat = [0] * 2048
for linha in open('input-05.txt'):
    row = int(linha[:7].replace('B', '1').replace('F', '0'), 2)
    column = int(linha[7:10].replace('R', '1').replace('L', '0'), 2)
    seat_id = row * 8 + column
    seat[seat_id] += 1
    #print(row, column, seat_id)
    if seat_id > max_seat_id:
        max_seat_id = seat_id
print(max_seat_id)

front = True
for i, s in enumerate(seat):
    #print(i, s)
    #continue
    if front and s:
        front = False
    elif not front and not s:
        print(i)
        break


