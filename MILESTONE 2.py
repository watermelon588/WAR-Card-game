# Global variable declare
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
# Creating a CARD CLASS.
class Card():
    def __init__(self,suits,ranks):
        self.suits = suits
        self.ranks = ranks
        self.values = values[ranks]
    def __str__(self):
        return self.ranks + " of " + self.suits
    
#TESTING ......

print("____________________________________________")

# Three_of_Hearts = Card("Hearts","Three")                # instance of card class object
# print(Three_of_Hearts.suits)                            # print suits      
# print(Three_of_Hearts.ranks)                            # print rank
# print(Three_of_Hearts.values)                           # print value
# print(Three_of_Hearts)                                  # print the card class object ..
# print("____________________________________________")

# Creating DECK CLASS.
class Deck():
    def __init__(self):

        self.all_cards_deck = []

        # run a for loop to append all the cards in all_cards.
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)    # Card is Created.
                self.all_cards_deck.append(created_card)
    # now we will create a function to shuffle all the card objects .
    def shuffle(self):
        random.shuffle(self.all_cards_deck)
    # now we will create a function to pick one  card from the shuffled cards.
    def pick_one_card(self):
        return self.all_cards_deck.pop()
    
new_deck = Deck()
new_deck.shuffle()
# TESTING .........
# for cards in new_deck.all_cards_deck:
#     print(cards)                                        # print all the cards in deck ..
# print("____________________________________________")   
# print(len(new_deck.all_cards_deck))                     # print the length of deck
# my_card = new_deck.pick_one_card()                      # pick a card
# print(my_card)                                          # print picked card
# print(len(new_deck.all_cards_deck))                     # print the length of the deck now
# for cards in new_deck.all_cards_deck:
#     print(cards)                                        # print all the cards in deck again ..
# print("____________________________________________")
# Creating Player Class
class Player():
    def __init__(self,name):
        self.name = name
        self.all_cards = []
    # add cards
    def add_cards(self,new_card):
        if type(new_card) == type([]):
            self.all_cards.extend(new_card)
        else:
            self.all_cards.append(new_card)
    # remove one card
    def remove_one_card(self):
        return self.all_cards.pop(0)
    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards"
    
# TESTING .........
# player_1=Player("Rohit")                        # player instance is created
# print(player_1)                                 # printing player class object
# player_1.add_cards(my_card)                     # add a single card in player_1
# print(player_1)                                 # print player class object again ...
# print(player_1.all_cards[0])                    # print the added card
# player_1.add_cards([my_card,my_card,my_card])   # add multiple cards in player_1
# print(player_1)                                 # print player class object again ...
# player_1.remove_one_card()                      # remove one card from player_1
# print(player_1)                                 # print player class object again ...

# GAME SETUP ...
player_one = Player(" GOJO ")           # player 1 instance is created .
player_two = Player(" GETO ")           # player 2 instance is created .

new_deck = Deck()                       # New Deck created .
new_deck.shuffle()                      # Shuffle the deck .

for x in range(26):
    player_one.add_cards(new_deck.pick_one_card())  # Split the deck into half and distribute.
    player_two.add_cards(new_deck.pick_one_card())
# GAME ON ...
game_on = True
round = 0

while game_on:
    round += 1                                          # Count the round number .
    print(f"Round : {round}")                           # Print each round .
    print(player_one)
    print(player_two)
    
    if len(player_one.all_cards) == 0:                  # Check if player 1 has any card left .
        print (f"{player_one}, out of cards !")
        print(f"{player_two} WINS !")
        game_on = False                                 # Out of the GAME .
        break
    if len(player_two.all_cards) == 0:                  # Check if player 2 has any card left .
        print (f"{player_two}, out of cards !")
        print(f"{player_one} WINS !")
        game_on = False                                 # Out of the GAME .
        break
    # START OF A NEW ROUND !
    player_1_cards_on_table = []                                  # Player 1 cards on the table .
    player_1_cards_on_table.append(player_one.remove_one_card())  # Remove a card and place on the table .
    player_2_cards_on_table = []                                  # Player 2 cards on the table .
    player_2_cards_on_table.append(player_two.remove_one_card())  # Remove a card and place on the table .

    # ... WAR ...

    at_war = True        # consider war is ON .
    while at_war:

        if player_1_cards_on_table[-1].values > player_2_cards_on_table[-1].values:
            player_one.add_cards(player_1_cards_on_table)
            player_one.add_cards(player_2_cards_on_table)

            at_war = False                                    # NOT A WAR !

        elif player_1_cards_on_table[-1].values < player_2_cards_on_table[-1].values:
            player_two.add_cards(player_1_cards_on_table)
            player_two.add_cards(player_2_cards_on_table)

            at_war = False                                    # NOT A WAR !

        else:
            print(" WAR !")

            if len(player_one.all_cards) < 5:               # If don't have enough(5) card , Can't participate in WAR .
                print(f"{player_one} is unable to participate in WAR ! GAME OVER at WAR !")
                print(f"{player_two} HAS WON !!")
                game_on = False                             # Out of the game .
                break
            elif len(player_two.all_cards) < 5:             # If don't have enough(5) card , Can't participate in WAR .
                print(f"{player_two} is unable to participate in WAR ! GAME OVER at WAR !")
                print(f"{player_one} HAS WON !!")
                game_on = False                             # Out of the game .
                break
            else :
                for n in range(5):                          # Draw out 5 cards each .
                    player_1_cards_on_table.append(player_one.remove_one_card())
                    player_2_cards_on_table.append(player_two.remove_one_card())

# End of the script .....
