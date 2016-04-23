

Deck = [('A', 'Clubs'), ('A', 'Dimes'), ('A', 'Hearts'), ('A', 'Spades'), ('K', 'Clubs'), ('K', 'Dimes'), ('K', 'Hearts'), ('K', 'Spades'), ('Q', 'Clubs'), ('Q', 'Dimes'), ('Q', 'Hearts'), ('Q', 'Spades'), ('J', 'Clubs'), ('J', 'Dimes'), ('J', 'Hearts'), ('J', 'Spades'), ('10', 'Clubs'), ('10', 'Dimes'), ('10', 'Hearts'), ('10', 'Spades'), ('9', 'Clubs'), ('9', 'Dimes'), ('9', 'Hearts'), ('9', 'Spades'), ('8', 'Clubs'), ('8', 'Dimes'), ('8', 'Hearts'), ('8', 'Spades'), ('7', 'Clubs'), ('7', 'Dimes'), ('7', 'Hearts'), ('7', 'Spades'), ('6', 'Clubs'), ('6', 'Dimes'), ('6', 'Hearts'), ('6', 'Spades'), ('5', 'Clubs'), ('5', 'Dimes'), ('5', 'Hearts'), ('5', 'Spades'), ('4', 'Clubs'), ('4', 'Dimes'), ('4', 'Hearts'), ('4', 'Spades'), ('3', 'Clubs'), ('3', 'Dimes'), ('3', 'Hearts'), ('3', 'Spades'), ('2', 'Clubs'), ('2', 'Dimes'), ('2', 'Hearts'), ('2', 'Spades')]

#converts card structures. Mode 1 converts from 'AD' to A Dimes. Mode 2 reverses it.
def card_converter(mode,cards):
    if mode == 1:
        for card in cards:
        
    if mode == 2:
        return 0

#Takes in user input for values of cards on table, returns list of cards
def card_input(cards):
    cardlist = []
    print "Please enter the cards by Number then Suit, in this format: \n If 8 of Diamonds, type in '8D'\n If Ace of Spades, type in 'AS'\n If Queen of Clubs, type in 'QC'\n"
    for i in range(0,cards):
        card = raw_input("Card no " + str(i+1) + ":\n")
        cardlist.append(card)
    return cardlist
    
#Takes in user input for number of players
def player_input():
    players = ""
    while(type(players)!= int):
        players = raw_input("How many players in total? (Eg. 5)\n")
        try:
            players = int(players)
        except:
            ValueError
    return players

#Takes in user input for number of cards on table, outputs list of cards
def river_cards_input():
    cards_out = ""
    valid_numbers = [0,3,4,5]
    while(cards_out not in valid_numbers):
        cards_out = raw_input("How many cards are out? (0, 3, 4 or 5) \n")
        try:
            cards_out = int(cards_out)
        except:
            ValueError
    if cards_out == 0:
        return 0
    else:
        return card_input(cards_out)

#Simulate texas holdem game
def texasholdemsim():
    players = player_input()
    river = river_cards_input()
    
    if stage == 0:
        return 0

