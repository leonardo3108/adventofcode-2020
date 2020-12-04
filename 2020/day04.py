passports = []
passport = {}
for linha in open('input-04.txt'):
    linha = linha.strip()
    if linha:
        campos = linha.split(' ')
        for campo in campos:
            field, value = campo.split(':')
            passport[field] = value
    else:
        passports.append(passport)
        passport = {}
passports.append(passport)

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
optional_fields = ['cid']

incompletes = 0
invalids = 0

def add_problem(passport, field, value):
    if 'problems' not in passport:
        passport['problems'] = []
    passport['problems'].append((field, value))
    
for passport in passports:
    for rf in required_fields:
        if rf not in passport:
            incompletes += 1
            passport['status'] = 'incomplete'
            #print('invalid:')
            break
    if 'status' not in passport:
        passport['status'] = 'valid'
        byr = passport['byr']
        if byr < '1920' or byr > '2002':
            add_problem(passport, 'byr', byr)
        iyr = passport['iyr']
        if iyr < '2010' or iyr > '2020':
            add_problem(passport, 'iyr', iyr)
        eyr = passport['eyr']
        if eyr < '2020' or eyr > '2030':
            add_problem(passport, 'eyr', eyr)
        hgt = passport['hgt']
        amount = int(hgt.replace('cm', '').replace('in', ''))
        unit = hgt[-2:]
        if unit not in ['cm','in'] \
           or unit == 'cm' and (amount < 150 or amount > 193) \
           or unit == 'in' and (amount < 59 or amount > 76):
            add_problem(passport, 'hgt', hgt)
        hcl = passport['hcl']
        valid_hcl = True
        if hcl[0] == '#' and len(hcl) == 7:
            for c in hcl[1:]:
                if (c < '0' or c > '9') and (c < 'a' or c > 'f'):
                    valid_hcl = False
                    break
        else:
            valid_hcl = False
        if not valid_hcl:
            add_problem(passport, 'hcl', hcl)
        ecl = passport['ecl']
        if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            add_problem(passport, 'ecl', ecl)
        pid = passport['pid']
        valid_pid = True
        if len(pid) == 9:
            for c in pid:
                if c < '0' or c > '9':
                    valid_pid = False
                    break
        else:
            valid_pid = False
        if not valid_pid:
            add_problem(passport, 'pid', pid)
        if 'problems' in passport:
            invalids += 1
            passport['status'] = 'invalid'
            print('passport invalid:', passport['problems'])
for passport in passports:
    pass
    #print(passport['status'])
    #print(passport)
print('total:', len(passports), ' incompletes:', incompletes, ' completes:', len(passports) - incompletes, 'valids', len(passports) - incompletes - invalids, ' invalids:', invalids)


#byr (Birth Year) - four digits; at least 1920 and at most 2002.
#iyr (Issue Year) - four digits; at least 2010 and at most 2020.
#eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
#hgt (Height) - a number followed by either cm or in:
#If cm, the number must be at least 150 and at most 193.
#If in, the number must be at least 59 and at most 76.
#hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
#ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
#pid (Passport ID) - a nine-digit number, including leading zeroes.
#cid (Country ID) - ignored, missing or not.