player = 0
cards = {1: [], 2:[]}

for line in open('input-22.txt'):
    line = line.strip()
    if 'Player 1:' in line:
        player = 1
    elif 'Player 2:' in line:
        player = 2
    elif line:
        cards[player].append(int(line))

#cards = {1: [9, 2, 6, 3, 1], 2:[5, 8, 4, 7, 10]}
print('=== First part ===')
original = {1: cards[1].copy(), 2: cards[2].copy()}
round = 0
winner_deck = []

while cards[1] and cards[2]:
    #print ('\tDecks: player 1', cards[1], '   player 2', cards[2])
    round += 1
    card1 = cards[1][0]
    card2 = cards[2][0]
    cards[1].remove(card1)
    cards[2].remove(card2)
    if card1 > card2:
        #print('Round', str(round) + ':  player 1 wins!', str(card1), 'x', str(card2))
        cards[1].append(card1)
        cards[1].append(card2)
        winner_deck = cards[1]
    else:
        #print('Round', str(round) + ':  player 2 wins!', str(card1), 'x', str(card2))
        cards[2].append(card2)
        cards[2].append(card1)
        winner_deck = cards[2]

#print()
score = sum([value * (len(winner_deck) - pos) for pos, value in enumerate(winner_deck)])
#print('Winner''s deck:', winner_deck)
print('Winner''s score:', score)

def game(cards, nr_game):
    nr_game += 1
    last_game = nr_game
    round = 0
    history = []
    while cards[1] and cards[2]:
        #print ('\tDecks: player 1', cards[1], '   player 2', cards[2])
        round += 1
        card1 = cards[1][0]
        card2 = cards[2][0]
        cards[1].remove(card1)
        cards[2].remove(card2)
        history.append(str(cards[1]) + ' x ' + str(cards[2]))
        if history[-1] in history[:-1]:
            #print('Game', str(nr_game), '- round', str(round) + ' - loop: player 1 wins the game!')
            return 1, cards[1], last_game
        #If both players have at least as many cards remaining in their deck as the value of the card they just drew, the winner of the round is determined by playing a new game of Recursive Combat
        if len(cards[1]) >= card1 and len(cards[2]) >= card2:
            #print('Round', str(round) + ':  recursive combat!')
            winner, _, last_game = game({1: cards[1][:card1].copy(), 2: cards[2][:card2].copy()}, last_game)
        elif card1 > card2:
            winner = 1
        else:
            winner = 2
        if winner == 1:
            #print('Game', str(nr_game), '- round', str(round) + ':  player 1 wins!', str(card1), 'x', str(card2))
            cards[1].append(card1)
            cards[1].append(card2)
        else:
            #print('Game', str(nr_game), '- round', str(round) + ':  player 2 wins!', str(card1), 'x', str(card2))
            cards[2].append(card2)
            cards[2].append(card1)
    if cards[1]:
        return 1, cards[1], last_game
    return 2, cards[2], last_game
    
#print()
print()
print('=== Second part ===')
cards = original
winner, deck, _ = game(cards, 0)
score = sum([value * (len(deck) - pos) for pos, value in enumerate(deck)])
print('Winner:', str(winner), ' score:', score)
