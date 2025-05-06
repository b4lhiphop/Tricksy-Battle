Tricksy Battle Game:
The game begins by giving the users each 8 cards/


### Rules for “Tricksy Battle”
• This game uses a standard deck of playing cards, with the Kings removed
– This results in a deck with 48 cards. (Ace, 2 through 10, Jack, Queen, in four “suits”.)
• The game starts with the deck face down (shuffled), and eight cards are dealt to each player.
    In this program each player is given a list with their hand
• The players keep their cards “in hand” (meaning they can see them), and private (meaning the
other player can’t see them).
    This feature is done via
• Every round, each player plays a card.
• One player starts by playing a card. This is called “leading”.
• At the start of the game, randomly determine who leads first.
• Whatever suit (hearts, diamonds, clubs, or spades) the player leads with, the other player must
follow, if possible.
• If the second player cannot play a card in the same suit, they can play any card they wish.
• The player with the highest-value card in the “lead” suit wins that round, and that player earns a
point.
• The player who wins the point gets to lead in the next round.
• After every round, one of the cards in the deck is removed and shown to both players. This has
no effect on scoring or points, other than giving players information about what cards the other
player might have.
• At the end of a round, if both players are down to four cards, they are each dealt four more cards.
This will happen twice in a game.
• The third time both players are down to 4 cards, the deck will also have 4 cards left. The players
do not draw any more, and just continue playing until they are out of cards.
• Ending the game:
– There are 16 rounds to the game, so there will be a total of 16 points if all rounds are played.
2
– If the game ends 16 to 0, the player with zero points has “shot the moon”, and immediately
scores 17 points, making them the winner.
– The player with the most points at the end of the game wins.
– If at any time one player reaches 9 points and the other player has at least 1 point, the game
should end, since there is no way the other player can still win.


### Run The Program
-- run at terminal with python tripsy_battle.py