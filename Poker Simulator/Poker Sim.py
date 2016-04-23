'''Poker'''
import random

Players = 5

'''Scoring'''
royalflush = 10
straightflush = 9
fourcards = 8
fullhouse = 7
flush = 6
straight = 5
threecards = 4
twopair = 3
pair = 2
highestcard = 1

Deck =['A Clubs', 'A Dimes', 'A Hearts', 'A Spades', 'K Clubs', 'K Dimes', 'K Hearts', 'K Spades', 'Q Clubs', 'Q Dimes', 'Q Hearts', 'Q Spades', 'J Clubs', 'J Dimes', 'J Hearts', 'J Spades', '10 Clubs', '10 Dimes', '10 Hearts', '10 Spades', '9 Clubs', '9 Dimes', '9 Hearts', '9 Spades', '8 Clubs', '8 Dimes', '8 Hearts', '8 Spades', '7 Clubs', '7 Dimes', '7 Hearts', '7 Spades', '6 Clubs', '6 Dimes', '6 Hearts', '6 Spades', '5 Clubs', '5 Dimes', '5 Hearts', '5 Spades', '4 Clubs', '4 Dimes', '4 Hearts', '4 Spades', '3 Clubs', '3 Dimes', '3 Hearts', '3 Spades', '2 Clubs', '2 Dimes', '2 Hearts', '2 Spades']

''' draw a card from deck without replacement'''
def drawcard(number):
    drawlist = []
    for draw in range(0,number):
        card = random.choice(Deck)
        drawlist.append(card)
        Deck.remove(card)
    return drawlist

'''draw hands for players'''
def hands(players):
    handlist = []
    for player in range(0,players):
        handlist.append(drawcard(2))
    return handlist

def river():
    return drawcard(3)

'''display hands line by line'''
def display(items):
    for hand in items:
        print hand
    return 0

'''splits up value and suit'''
def cardproc(cards):
    cardlist = []
    for card in cards:
        store = card.split(" ")
        cardlist.append((store[0],store[1]))
    return cardlist

'''If flush present, return TRUE'''
def flushcheck(cards):
    suit = []
    for card in cards:
        suit.append(card[1])
    suits = list(set(suit))
    for cardsuit in suits:
        count = suit.count(cardsuit)
        if count > 5:
            return cardsuit
    return None
        
    
'''If royal flush, returns TRUE'''
def royalflush(cards):
    royal = ['A','K','Q','J','10']
    value = []
    for card in cards:
        value.append(card[0])
    if set(royal).issubset(set(value)):
        return True
    return False
    
def anystraight(cards):
    return 0

'''Simulates hand pairs and their occurrence'''
def pairhandsim(players, iterations = 1000,valuereq = None):
    games = []
    for i in range(0,iterations):
        gamepairs = 0
        x = hands(players)
        for y in x:
            a = []
            for z in y:
                a.append(z.split(" "))
            if a[0][0] == a[1][0]:
                if valuereq:
                    if a[0][0] == str(valuereq):
                        gamepairs += 1
                else:
                    gamepairs += 1
        games.append(gamepairs)
        for b in x:
            for c in b:
                Deck.append(c)

    f = {}
    for i in range(0,Players+1):
        f[i] = 0
        for j in games:
            if i == j:
                f[i] += 1
    print 'Number of pairs: Number of times it appeared \n'
    print f

def texasholdemplay(players):
    gameriver = river()
    gamehands = hands(players)
    count = 3
    while (count <5):
        display(gamehands)
        if count == 3:
            print '\n Dealing river...'
        print gameriver
        x = raw_input("\n Draw? (Y/N)")
        if x.upper() == "Y":
            gameriver.append(drawcard(1)[0])
            count += 1
        else:
            if x.upper() == "N":
                print "\n Ok, terminating program..."
                return 0
            else:
                print " ----------------- \n INVALID CHOICE \n -----------------"
    display(gamehands)
    print gameriver
    return 0

'''Outputs desired criteria'''
def SimOutput(hands, criteria = 'pair'):
    for hand in hands:
        print 0


