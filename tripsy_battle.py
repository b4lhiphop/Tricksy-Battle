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
lead = random.choice(["player1", "player2"])
while rounds < 16:  
    print(f"{lead} has been selected to go first")
#TODO Make a function that plays a card. It takes a random card from the hand and puts in the players hand then deletes the card from the deckdef play_round(player1_hand,player2_hand):
    if lead == "player1":
        lead_hand =player1_hand
        response_player_hand = player2_hand
        response_player = "player2"
        query = input(f"{response_player} look away. {lead} press anything on your keyboard + enter to see your deck")
        print(lead_hand)
        choice = get_choice(lead_hand, lead)       
        lead_card = player1_hand.pop(choice)
        lead_suit = get_suit(lead_card)

    
    elif lead == "player2":
        lead_hand = player2_hand
        response_player_hand = player2_hand
        response_player = "player1"
        query =input(f"{response_player} look away. {lead} press anything on your keyboard + enter to see your deck: ")           
        print(lead_hand)
        choice = get_choice(lead_hand, lead) 
        lead_card = player2_hand.pop(choice)
        lead_suit = lead_card.get_suit(lead_card)
    #TODO Get value of lead card 
    lead_card_value = get_value(lead_card)
    lead_card_string = print_card(lead_card)
    print(f"{lead} has pulled out {lead_card_string} with a value of {lead_card_value}")
    temp_hand = create_suit_deck(response_player_hand, lead_suit)
    if len(temp_hand)== 0:
        query = input(f"{response_player} look away. {lead} press anything on your keyboard + enter to see your deck")
        print("You have no matching suites. Pick a card from your whole deck")
        print(response_player_hand)
        choice = get_choice(response_player_hand, response_player)
        response_card = player1_hand.pop(choice)
    else:
        query = input(f"{lead} look away. {response_player} press anything on your keyboard + enter to see your deck")
        print(f" This is your full hand: {response_player_hand}. \n Your may pick from cards with the lead card suit {lead_suit}. \n Here is a list of all of your options: {temp_hand}")
        choice = get_choice(response_player_hand, response_player)
        response_card = temp_hand.pop()
        int = find_int(response_card,response_player_hand)
        response_player_hand.pop(int)




        
        
        
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
def get_suit(card):
    """
    Takes in card tuple and returns suit
    """
    return card[1]
def create_suit_deck(deck, suit):
    """
    Creates A deck with selected suits
    """
    new_deck = []
    for card in deck:
        if card[1] == suit:
            new_deck.append(card)
    return new_deck
def play_game():
    pass
def get_choice(hand, player):
    while True:
            try:
                choice = int(input(f"{player} please select a card from your hand above Play a card. Input index starting from 0: "))
                while choice > len(hand):
                    print("Please try again. You typed an int outside of scope.")
                    choice = int(input(f"{player} please select a card from your hand above Play a card. Input index starting from 0: "))
                break
            except:
                print("please try again. You did not type a valid integer ")
def find_int(card, hand):
    '''
    
    '''
    i = 0
    while(i < len(hand)):
        if hand[i] == card:
            final_index = i
            return i
        else:
            return -1
    
        
card = ("Queen", "Spades")
card[0]
get_value(card=card)
print_card(card= card)
suit =get_suit(card=card)
print(suit)

# 
#  




