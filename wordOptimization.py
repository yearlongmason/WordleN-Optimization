# Project: Wordle-N Optimization
# wordOptimization.py
# Test and score words to find the optimal starting word.
# Created / Modified by: Thomas Smith

from algorithm import astar
from wordleN import WordleN
from organizeData import getWordsOfLengthN

""" This function should take a word, and test is as a starting word using our algorithm.
    The starting word will be tested with every possible goal word, and its score will be
    the total number of guesses it took to solve each puzzle (lower score is, of course, better)."""
def scoreWord(word: str) -> int:
    score: int = 0
    wordLength: int = len(word)
    goalWords: list[str] = getWordsOfLengthN(wordLength)

    for goalWord in goalWords:
        testGame: WordleN = WordleN(wordLength)
        testGame.startWord = word
        testGame.goalWord = goalWord
        solution = astar(testGame)
        guesses = len(solution)
        print(goalWord + " - " + str(guesses))
        score += guesses

    return score

""" This function should take an integer, and return a list of all words of that length,
    and their scores.
    !!! THIS WILL TAKE YEARS TO RUN BE CAREFUL !!!"""
def checkWordsOfLengthN(length: int) -> list[tuple[str, int]]:
    wordsToTest: list[str] = getWordsOfLengthN(length)
    scores: list[tuple[str, int]] = []

    for wordToTest in wordsToTest:
        score: int = scoreWord(wordToTest)
        scores.append((wordToTest, score))

    return scores


if __name__ == '__main__':
    scoredWords = checkWordsOfLengthN(20)
    list.sort(scoredWords, key = lambda tup: tup[1], reverse = True)

    for w in scoredWords:
        print(w[0] + ": " + str(w[1]))