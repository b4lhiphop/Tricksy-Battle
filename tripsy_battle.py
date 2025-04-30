import random
#TODO Make a Deck of 48 Cards Using A dictionary using a list wit tuples

cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9","10", "Jack", "Queen"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
deck = []
for card in cards:
    for suit in suits:
        deck.append((card,suit))
print(deck)
#TODO Make a list with thier current hand
random.shuffle(deck)
print(deck)
player1_hand = []
player2_hand = []
i = 0
#TODO Give each player eight cards
for i in range(8):
    player1_hand.append(deck.pop())
    player2_hand.append(deck.pop())
    i+= 1
player1_hand

#TODO use random to decide which player will pick first
rounds = 0
while rounds < 16:
    lead = random.choice(["player1", "player2"])  
    if lead == "player1":
        response_player =  "player2"
    else:
        response_player = "player1"
    
    print(f"{lead} has been selected to go first")
#TODO Make a function that plays a card. It takes a random card from the hand and puts in the players hand then deletes the card from the deck
    if lead == "player1":
        lead_hand =player1_hand
        choice = input(f"{lead} please select a card from your hand above Play a card. Input index starting from 0") # Fix instructions at some point
        lead_card = player1_hand.pop(choice)
    
    elif lead == "player2":
        player_2_hand = input
        choice = input(f"{lead} please select a card from your hand above Play a card. Input index starting from 0") # Fix instructions at some point
        lead_card = player2_hand.pop(choice)
    #TODO Get value of lead card 
    lead_card = ("Queen", "Spades")
    lead_card_value = get_value(lead_card)
    lead_card_string = print_card(card)
    print(f"{lead} has pulled out {lead_card_string}")


    

    

    rounds += 1




    


#TODO use random to decide which player will pick first

#TODO show selected player their cards and ask them to pick a card to play

def play_card():
    """
    This function takes 
    """

    pass
def get_value(card):
    """
    This function takes a card tuple as a parameter and returns its value.
    """
    if "Ace" in card[0]:
        return 1
    elif "2" in card[0]:
        return 2 
    elif "3" in card[0]:
        return 3
    elif "4" in card[0]:
        return 4
    elif "5" in card[0]:
        return 5
    elif "6" in card[0]:
        return 6
    elif "7" in card[0]:
        return 7
    elif "8" in card[0]:
        return 8
    elif "9" in card[0]:
        return 9
    elif "10" in card[0]:
        return 10
    elif "Jack" in card[0]:
        return 11
    elif "Queen" in card[0]:
        return 12
def print_card(card):
    """
    Takes in card tuple and returns a string for the card to be printed
    """
    card_string = str(card[0] +" of "+ card[1])
    return card_string

card = ("Queen", "Spades")
card[0]
get_value(card=card)
print_card(card= card)



# 
#  




