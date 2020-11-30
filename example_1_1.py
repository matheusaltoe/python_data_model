import collections
from random import choice 

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                       for rank in self.ranks]
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]   


# Deck cards number
deck = FrenchDeck()
print('Deck cards number: %r') % len(deck)

# Deck cards position
print(deck[0])
print(deck[-1])

# Choice random card
print(choice(deck))

# First three cards
print(deck[:3])

# Iterable deck
for card in deck:
    print(card)

# Reverse Iterable deck
for card in reversed(deck):
    print(card)  

#Card in deck
if Card('Q', 'hearts') in deck:
    print(True)

#Card not in deck
if not Card('7', 'beasts') in deck:
    print(False)

#Order cards
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)