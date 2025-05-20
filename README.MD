## Tricksy Battle
### A game of chance and skill

## Overview
For INST 126 I created a card game called Tricksy Battle. This game requires two players who both begin with eight cards. A lead player is randomly selected and plays a card. The responding player is then required to respond with a card that matches the same suite, or to discard a card if no matching suite is find within thier deck. Whichever player plays the card with the highest point total in the lead suite is the winner for that round. The player who wins that rounds get gets to lead next round. This proccess repeats for a maximum of 16 rounds. Every round, one of the cards from the deck gets removed and is shown to both players. The game ends early on the special condition that one player has 9 points and the other player has at least one in which the player with 9 points will be announced the winner. At the end of the game the player with the most points will win unless if one player scores 16 points. In this case the player with 0 points will recieve 17 points and is considered the winner. This program simulates this game and process. 

 More detailed rules are detailed below:
### Rules for “Tricksy Battle”
**Two Players Are Required**

### How to run Game
**Clone Repository using git**
**Enter python tripsy_battle.py into terminal**
**Follow instructions to play game**

### Special Features
**time library**
1. Used in game_countdown() function to create countdown effect.
2. Used throughout the game to give users time to see scores and slow down the functioning of the game which makes it more user friendly.
**random library**
1. Used in the begginng of the game to decide which player will lead first.
2. Used to shuffle the deck at the beggining of the game
**Matplotlib library**
1. Used at the end of the game to plot to represent the scores of each player on a graph

