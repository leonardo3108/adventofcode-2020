tickets = ''
nearby_tickets = []
fields = {}
invalid_values = []
valid_tickets = []
valid_columns = {}

for linha in open('input-16.txt'):
    if 'ticket' in linha and ':' in linha:
        tickets = linha.strip().strip(':')
    elif ':' in linha:
        field, ranges = linha.strip().split(':')
        range1, _, range2 = ranges.strip().split()
        init1, end1 = [int(x) for x in range1.split('-')]
        init2, end2 = [int(x) for x in range2.split('-')]
        fields[field] = (init1, end1, init2, end2)
        valid_columns[field] = []
    elif ',' in linha:
        seats = [int(x) for x in linha.strip().split(',')]
        if tickets == 'your ticket':
            your_ticket = seats
        elif tickets == 'nearby tickets':
            nearby_tickets.append(seats)

#print(nearby_tickets)
#print(your_ticket)
for field in fields.keys():
    print(field, fields[field])


error_rate = 0
for ticket in nearby_tickets:
    ticket_status = 'valid'
    for value in ticket:
        status = 'invalid'
        for field in fields.keys():
            init1, end1, init2, end2 = fields[field]
            if value >= init1 and value <= end1 or value >= init2 and value <= end2:
                status = 'valid'
                break
        if status == 'invalid':
            invalid_values.append(value)
            error_rate += value
            ticket_status = 'invalid'
    if ticket_status == 'valid':
        valid_tickets.append(ticket)

print()
#print(sorted(invalid_values))
print('error rate', error_rate)
print('valid tickets:', len(nearby_tickets), '-->', len(valid_tickets))

for field in fields.keys():
    init1, end1, init2, end2 = fields[field]
    #print('field:', field, init1, end1, init2, end2)
    for order in range(0, len(your_ticket)):
        #print('\torder:', order)
        valid_column = True
        for ticket in valid_tickets:
            value = ticket[order]
            #print('\t\tvalue:', value)
            if value >= init1 and value <= end1 or value >= init2 and value <= end2:
                pass
            else:
                valid_column = False
            #print('\t\tvalid:', valid_column)
            if not valid_column:
                break
        if valid_column:
            valid_columns[field].append(order)
            #print('valid!', 'field:', field, '  order:', order)

order1 = ['']*len(valid_columns)
order2 = ['']*len(valid_columns)
for field in valid_columns:
    order1[len(valid_columns[field])-1] = field

used_columns = []
for field in order1:
    for column in valid_columns[field]:
        if column not in used_columns:
            order2[column] = field
            used_columns.append(column)
print('fields order:', order2)

answer = 1
for i, field in enumerate(order2):
    if 'departure' in field:
        print (i, field, your_ticket[i])
        answer *= your_ticket[i]

print('answer:', answer)    