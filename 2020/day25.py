#from math import log, ceil, pow

card_public, door_public = [int(line.strip()) for line in open('input-25.txt')]
initial_subject_number = 7
divider = 20201227

#card_public, door_public = 5764801, 17807724 

print('initial_subject_number', initial_subject_number, 'divider', divider)

def transform(subject_number, key, divider):
    return pow(subject_number, key, divider)

def decript(subject_number, public_key, divider):
    secret_key = 0
    while transform(subject_number, secret_key, divider) != public_key:
        secret_key += 1
    return secret_key

print('card public', card_public, 'door public', door_public)

print('Decripting secrets...')
card_secret = decript(initial_subject_number, card_public, divider)
print('\tcard secret:', card_secret)

encryption_key = transform(door_public, card_secret, divider)

print('encryption key', encryption_key)

