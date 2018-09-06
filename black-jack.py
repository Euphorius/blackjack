from random import shuffle
from test import points

class Deck:

    def __init__(self, deck=[], faces=['J', 'Q', 'K', 'A'], numbers=[x for x in range(2,11)]):
        self.deck = deck
        self.faces = faces
        self.numbers = numbers
        numbers.extend(faces)

        for suit in ['Spades', 'Hearths', 'Diamonds', 'Clubs']:
            for num in numbers:
                deck.append(str(num) + ' of ' + str(suit))

        shuffle(deck)
        
class Dealer:

    def __init__(self, hand):
        self.hand = hand

class Player:

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
class Engine(Player):

    def __init__(self):
        pass

    def score(self, hand):
        score = 0
        for card in hand:
            score += points[card]

        if hand[0][0] == "A" or hand[1][0] == "A":
            print("Player score: ", score, " / ", score - 10)
        
    def draw_card(self, hand):
        hand.append(deck.deck.pop())

    def check_winner(self, player_name, player, dealer):
        if Engine().score(player) > Engine().score(dealer):
            print (f'{player_name} wins')
        elif Engine().score(player) == Engine().score(dealer):
            print("It's a tie")
        else:
            print("Dealer wins!")

    def split(self, hand):
        pass

deck = Deck()
phand = list()
dhand = list()

for i in range(2):
    phand.append(deck.deck.pop())
    dhand.append(deck.deck.pop())

player = Player("Stoycho", phand)
dealer = Dealer(dhand)
engine = Engine()