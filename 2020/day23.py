input = '789465123'
moves = 100
input = '389125467'
#moves = 10
game = 2

class Cup:
    value = 0
    next = previous = None
    def __init__(self, value, previous):
        self.value = value
        if previous:
            previous.set_next(self)
    def set_next(self, next):
        self.next = next
        if next:
            next.previous = self
    def __str__(self):
        return str(self.value)

class Circle:
    current = first = None
    min_value = 99
    max_value = 0
    cups = []
    small = True
    def __init__(self, text):
        last = None
        for c in text:
            value = int(c)
            self.cups.append(Cup(value, last))
            last = self.cups[-1]
            if value > self.max_value:
                self.max_value = value
            elif value < self.min_value:
                self.min_value = value
        self.first = self.current = self.cups[0]
        last.set_next(self.first)
    def __str__(self):
        if self.small:
            text = ''
            for cup in self.cups:
                if cup == self.current:
                    text += '(' + str(cup) + ') '
                else:
                    text += str(cup) + ' '
            return text[:-1]
        else:
            return self.neighborhood(1, 4)
    def get_cup(self, value):
        for cup in self.cups:
            if cup.value == value:
                return cup
        return None
    def pick_up(self):
        first = self.current.next
        #pick up
        self.current.set_next(first.next.next.next)
        self.cups.remove(first.next.next)
        self.cups.remove(first.next)
        self.cups.remove(first)
        destination_value = self.current.value - 1
        pick_up_values = [first.value, first.next.value, first.next.next.value]
        #next current
        self.current = self.current.next
        #find destination
        while True:
            if destination_value in pick_up_values:
                destination_value -= 1
            elif destination_value < self.min_value:
                destination_value = self.max_value
            else:
                break
        first.next.next.set_next(None)
        destination_cup = self.get_cup(destination_value)
        #reinsert pick-up
        next = destination_cup.next
        next_pos = self.cups.index(next)
        destination_cup.set_next(first)
        first.next.next.set_next(next)
        self.cups.insert(next_pos, first.next.next)
        self.cups.insert(next_pos, first.next)
        self.cups.insert(next_pos, first)
        return pick_up_values, destination_value
    def add_value(self, value):
        cup = Cup(value, None)
        cup.set_next(self.current)
        self.cups.append(cup)
        self.small = False
    def neighborhood(self, value, qtty):
        center = cup = self.get_cup(value)
        text = str(cup)
        for i in range(qtty):
            cup = cup.next
            text += ' ' + str(cup)
        cup = center
        for i in range(qtty):
            cup = cup.previous
            text = str(cup) + ' ' + text
        return text
move = 0
if game == 1:
    circle = Circle(input)
    while move < moves:
        move += 1
        #print('\n-- move', move, '--')
        #print('cups:', circle)
        pick_up_values, destination = circle.pick_up()
        #print('pick up:', str(pick_up_values)[1:-1])
        #print('destination:', destination)
    #print('\n-- final --')
    #print('cups:', circle)
    pos1 = pos = circle.get_cup(1)
    text = ''
    pos = pos.next
    while pos != pos1:
        text += str(pos.value)
        pos = pos.next
    print('labels:', text)
    exit()

print('input:', input)
circle = Circle(input)
for value in range(circle.max_value + 1, 1000001):
    circle.add_value(value)
print('cups:', circle)
moves = 10000000
while move < moves:
    move += 1
    if move % 1000 == 0:
        if move == 1000:
            print('\tmoves: 1 thousand.')
        else:
            print('\tmoves:', move // 1000, 'thousands.')
    pick_up_values, destination = circle.pick_up()
print('cups:', circle)
star_cup1 = circle.get_cup(1).next
star_cup2 = star_cup1.next
print('start cups:', star_cup1.value, 'and', star_cup2.value, ' - product:', star_cup1.value * star_cup2.value)

