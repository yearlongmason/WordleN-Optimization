# Project: Wordle-N Optimization
# wordOptimization.py
# Test and score words to find the optimal starting word.
# Created / Modified by: Thomas Smith, Mason Lee

from algorithm import astar
from wordleN import WordleN
from organizeData import getWordsOfLengthN
import numpy as np

""" This function should take a word, and test it as a starting word using our algorithm.
    The starting word will be tested with a sample of every possible goal word, and its score will be
    the average number of guesses it took to solve each puzzle (lower score is, of course, better)."""


def scoreWord(word: str, sampleSize: int) -> int:
    score: int = 0
    wordLength: int = len(word)
    goalWords: list[str] = getWordsOfLengthN(wordLength)

    # If the user chooses a sample size larger than the length of goal words
    if sampleSize > len(goalWords):
        sampleSize = len(goalWords)

    # Get a sample of goal words
    goalWords = np.random.choice(goalWords, sampleSize, replace=False)

    # Loop through all goal words and simulate a game of wordle
    # Add the number of guesses to the score
    for goalWord in goalWords:
        testGame: WordleN = WordleN(wordLength)
        testGame.startWord = word
        testGame.goalWord = goalWord
        solution = astar(testGame)
        guesses = len(solution)
        print(f"{word} -> {goalWord} = {str(guesses)} guesses")
        score += guesses

    # Return the average number of guesses for the word
    return score / sampleSize


""" This function should take an integer, and return a list of all words of that length,
    and their scores.
    !!! THIS WILL TAKE YEARS TO RUN BE CAREFUL !!!"""


def checkWordsOfLengthN(length: int, sampleSize=10) -> list[tuple[str, int]]:
    # Get all words of length N
    wordsToTest: list[str] = getWordsOfLengthN(length)
    scores: list[tuple[str, int]] = []

    # Loop through each word, give it a score and append it to scores
    for wordToTest in wordsToTest:
        score: int = scoreWord(wordToTest, sampleSize)
        scores.append((wordToTest, score))

    # Sort scores based on score
    list.sort(scores, key=lambda tup: tup[1], reverse=True)

    return scores


if __name__ == '__main__':
    # Begin Comment here for Specific Word Score
    choice: int
    while True:
        choice = int(input("What would you like to do?\n 1. Starting Words \n 2. Word Scoring \n 3. Exit"))
        if choice == 1:
            # CAUTION: Using word lengths between 3 and 19 will likely take a VERY long time to run
            wordLength = int(input("What length word would you like to search through? "))
            sampleSize = int(
                input("What would you like the sample size to be? (we recommend 5-10 because of runtime issues) "))
            scoredWords = checkWordsOfLengthN(wordLength, sampleSize)

            print("\nWord : Average number of guesses")
            for word in scoredWords:
                print(f"{word[0]}: {word[1]}")

        elif choice == 2:
            # Find Specific Words Score:
            word = input("Enter the word you would like to score: ")
            sampleSize = int(input("What would you like the sample size to be? "))
            score = scoreWord(word, sampleSize)
            print(f"{word} takes an average of {score} guesses to solve")

        elif choice == 3:
            break
