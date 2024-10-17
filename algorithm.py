# Project: Wordle-N Optimization
# algorithm.py
# Implement a version of A* to search through Wordle-N words.
# Created / Modified by: Mason Lee, Thomas Smith

from wordleN import WordleN
from colorama import Back, Style

"""This function should contain the main algorithm we use to play through a game.
    Parameters:
    wordleGame: An instance of WordleN that will keep track of game state information 
    such as possible words, start word, and goal word
    
    Should return a list of words that were guessed to get to the goalWord"""
def astar(wordleGame: WordleN) -> list[str]:
    guessList: list[str] = [] # List of guessed words
    # Loop until goalWord is found
    # Guess next best word from possible words (highest heuristic)
    # If the next best word is not the correct word, get the clues for the game from checkWord function
    # Then trim self.possibleWords using cleanup_list
    # Update heuristic by calling letterFrequency

    currentGuess = wordleGame.startWord
    guessList.append(wordleGame.startWord)
    while currentGuess != wordleGame.goalWord:
        # generate clues for current guess and narrow down list of possible guesses
        currentClues = wordleGame.checkWord(currentGuess)
        wordleGame.cleanup_list(currentGuess, currentClues)
        #wordleGame.letterFrequency()

        # generate heuristic for each possible word, save the best heuristic as next guess
        # this is the equivalent of a priority queue
        bestGuess: str = ''
        bestHeuristic: int = 0
        for guess in wordleGame.possibleWords:
            heuristic = wordleGame.generateHeuristic(guess.lower())
            if heuristic > bestHeuristic:
                bestHeuristic = heuristic
                bestGuess = guess

        guessList.append(bestGuess)
        currentGuess = bestGuess
    return guessList

"""This function is meant to display the path the algorithm took to get from
the start word to the goal word using colorama to show Wordle clues"""
def displaySolution(solution: list[str]):
    display_list = []
    for word in solution:
        colored_word = ""
        for char in range(len(word)):
            if word[char] == solution[-1][char]:
                colored_word += Back.GREEN + word[char]
            elif word[char] in solution[-1]:
                colored_word += Back.YELLOW + word[char]
            else:
                colored_word += Back.LIGHTBLACK_EX + word[char]
        colored_word += Style.RESET_ALL
        display_list.append(colored_word)
    for word in display_list:
        print(word)

if __name__ == "__main__":
    # TEST CODE GOES HERE
    testGame = WordleN(5)
    testGame.startWord = 'slate'
    testGame.getRandomGoalWord()

    solution = astar(testGame)
    print("Starting word: " + testGame.startWord)
    print("Goal word: " + testGame.goalWord)
    print("Solved in " + str(len(solution)) + " guesses")
    print("\n")
    print("Guesses: ")
    displaySolution(solution)
