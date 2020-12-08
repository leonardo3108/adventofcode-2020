instruction = []
for linha in open('input-08.txt'):
    operation , argument = linha.strip().split()
    instruction.append((operation , int(argument)))

program_size = len(instruction)
def execute(instruction):
    instr_add = 0
    accumulator = 0
    executed = []
    while (True):
        next_instr = instruction[instr_add]
        #print(instr_add, next_instr, accumulator)
        executed.append(instr_add)
        if next_instr[0] == 'jmp':
            instr_add += next_instr[1]
        else:
            instr_add += 1
            if next_instr[0] == 'acc':
                accumulator += next_instr[1]
        if instr_add in executed:
            return ('loop', accumulator, executed)
        if instr_add == program_size:
            return ('end', accumulator, None)


def adjust_execution(executed, change):
    if change < 0:
        adjust = instruction.copy()
        last_instruction = instruction[executed[change]]
        if last_instruction[0] == 'jmp':
            adjust[executed[change]] = ('nop', last_instruction[1])
        elif last_instruction[0] == 'nop':
            adjust[executed[change]] = ('jmp', last_instruction[1])
        else:
            print(change, instruction[executed[change]], '<nop>')
            return 'acc', 0, None
        print(change, instruction[executed[change]], '->', adjust[executed[change]])
        return execute(adjust)
    return execute(instruction)


result = ''
executed = None
first = None
change = 0
while result != 'end':
    result, acc, executed = adjust_execution(first, change)
    if result != 'acc':
        print(acc, '(' + result + ')')
        if not change:
            first = executed
    change -= 1