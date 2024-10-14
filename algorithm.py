# Project: Wordle-N Optimization
# algorithm.py
# Implement a version of A* to search through Wordle-N words.
# Created / Modified by: Mason Lee

import wordleN

"""This function should contain the main algorithm we use to play through a game.
    Parameters:
    wordleGame: An instance of WordleN that will keep track of game state information 
    such as possible words, start word, and goal word
    
    Should return a list of words that were guessed to get to the goalWord"""
def astar(wordleGame) -> list[str]:
    guessList: list[str] = [] # List of guessed words
    # Loop until goalWord is found
    # Guess next best word from possible words (highest heuristic)
    # If the next best word is not the correct word, get the clues for the game from checkWord function
    # Then trim self.possibleWords using cleanup_list
    # Update heuristic by calling letterFrequency
    pass

if __name__ == "__main__":
    # TEST CODE GOES HERE
    pass