# 3-Card Poker Game - Unit Testing

This lab introduced us to Unit Testing and its best practices. Specifically, we needed to write a handful of unit tests using assertEqual from the unittest library that verified the game functions we wrote worked as expected.

The most difficult part of this assignment was writing the game functions correctly and coding in the win conditions correctly. First, we had to figure out how to derive an integer value for each card played so that their actual game values could be compared. This involved creating two tuples: one containing the list of cards in sequential order, one containing the corresponding card values in sequential order. Card value could then be derived from the index position of the card played in the original tuple. After deriving values, we then could compare those values according to the game instructions to complete our game functions.

This game cannot actually be played, only unit tested.
