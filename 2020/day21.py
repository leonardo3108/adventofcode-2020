input = [line.strip() for line in open('input-21.txt')]

foods = []
for line in input:
    parts = line.rstrip(')').split('(')
    ingredients = parts[0].rstrip().split()
    alergens = [allergen.rstrip(',') for allergen in parts[1].rstrip().split()[1:]]
    foods.append((ingredients, alergens))

all_ingredients = []
all_allergens = []
food_ingredients = {}
food_alergens = {}
for i, (ingredients, alergens) in enumerate(foods):
    food_ingredients[i] = ingredients
    for ingredient in ingredients:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)
    food_alergens[i] = alergens
    for allergen in alergens:
        if allergen not in all_allergens:
            all_allergens.append(allergen)

all_ingredients = sorted(all_ingredients)
all_allergens = sorted(all_allergens)
print('All ingredients:', all_ingredients)
print('All alergens:', all_allergens)
print()

possible = {}
causes = {}
causes['any'] = []
for allergen in all_allergens:
    possible[allergen] = []
    causes[allergen] = []
    for i, (ingredients, alergens) in enumerate(foods):
        if allergen in alergens:
            possible[allergen].append(i)
    for ingredient in all_ingredients:
        qt = 0
        for i in possible[allergen]:
            qt += ingredient in food_ingredients[i]
        if qt == len(possible[allergen]):
            causes[allergen].append(ingredient)
            if ingredient not in causes['any']:
                causes['any'].append(ingredient)
    print('Possible causes for', allergen + ':', causes[allergen])
print('Possible causes for any alergy:', causes['any'])

all_ocurrencies = 0
for ingredient in all_ingredients:
    if ingredient not in causes['any']:
        ocurrencies = 0
        for ingredients, _ in foods:
            ocurrencies += ingredient in ingredients
            all_ocurrencies += ingredient in ingredients
print()
print('Inert ingredients - all ocurrencies in foods:', all_ocurrencies)

print()
exclusive = {}
#For part 2 is was just seeing which allergen matched 1 ingredient, then removing said ingredient from the other allergens until each one was resolved to only having 1 known ingredient. A sorted dictionary made light work of the final string result.
qttys = [len(causes[allergen]) for allergen in all_allergens]
while 1 in qttys:
    allergen = all_allergens[qttys.index(1)]
    ingredient = causes[allergen][0]
    exclusive[allergen] = ingredient
    print('Exclusive causes for', allergen + ':', ingredient)
    for other in all_allergens:
        if ingredient in causes[other]:
            causes[other].remove(ingredient)
    qttys = [len(causes[allergen]) for allergen in all_allergens]


print()
print('Canonical list:', ','.join([exclusive[allergen] for allergen in all_allergens]))
