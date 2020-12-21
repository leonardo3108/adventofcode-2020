expressions = [linha.strip() for linha in open('input-18.txt')]

def find_parentesis(expression):
    o = expression.find('(')
    openings = []
    while o >= 0:
        openings.insert(0, o)
        o = expression.find('(', o+1)
    closing = {}
    closings = []
    for opening in openings:
        c = expression.find(')', opening)
        while c in closings:
            c = expression.find(')', c+1)        
        closings.append(c)
        closing[opening] = c
    return closing, openings

def evaluate(expression, show, mode):
    operation = ''
    parts = expression.split()
    if mode == 'order':
        result = 0
        for part in parts:
            if part == '+' or part == '*':
                operation = part
            elif operation == '+':
                result += int(part)
            elif operation == '*':
                result *= int(part)
            else:
                result = int(part)
    elif mode == '+':
        while '+' in parts:
            pos = parts.index('+')
            value = int(parts[pos-1]) + int(parts[pos+1])
            parts.insert(pos-1, str(value))
            del parts[pos]
            del parts[pos]
            del parts[pos]
        result = 1
        for v in parts[::2]:
            result *= int(v)
    if show:
        print('\tevaluate', expression, '-->', result)
    return result
    
def process(expression, show, mode):
    if show:
        print()
        print(expression)
    closing, openings = find_parentesis(expression)
    #print('\tparentesis:', closing, openings)
    expr = expression
    while openings:
        next_opening = openings[0]
        if '(' in expr:
            value = evaluate(expr[next_opening+1:closing[next_opening]], show, mode)
            reduction = len(expr)
            expr = expr[:next_opening] + str(value) + expr[closing[next_opening]+1:]
            reduction -= len(expr)
            if show:
                print('\t', expr)#, reduction)
            for opening in openings:
                if closing[opening] > closing[next_opening]:
                    closing[opening] -= reduction
            openings.remove(next_opening)
            del closing[next_opening]
            #print('\tparentesis:', closing, openings)
    else:
        return evaluate(expr, show, mode)

sum = 0
for expression in expressions:
    sum += process(expression, False, 'order')
print(sum)
    
sum = 0
for expression in expressions:
    sum += process(expression, False, '+')
print(sum)
