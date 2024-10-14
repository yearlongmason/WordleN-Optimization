# Project: Wordle-N Optimization
# organizeData
# Grab data from english.xlsx and sort into different text files based on word length
# e.g. wordle6Data.txt would have all 6 letter words
# Created / Modified by: Mason Lee

import pandas as pd

"""This function grabs data from a csv and returns all words"""
def getAllWords():
    
    # Get data from csv
    data = pd.read_csv("Data/scrabbleWords.csv")
    
    # Get words as their own list
    words = list([str(x).lower() for x in data["word"]])
    
    return words
    
"""Sorts all words into their own files arranged by length"""
def sortWords(words: list[str]) -> dict[int, list[str]]:
    
    # Create dictionary storing length and list of words pairs
    # Only storing words whose length are between 2 and 20 characters long
    wordsByLength = {}
    
    # Loop through each word
    for word in words:
        
        # If the word's length does not exist in the dictionary, it is not being recorded
        if len(word) not in wordsByLength.keys():
            wordsByLength[len(word)] = [word]
        
        # If it does exist, just add it to it's respective list
        wordsByLength[len(word)].append(word)
        
    # By the end of the loop we have a dictionary of lists formatted as:
    # {lengthOfWord : listOfAllWordsOfThatLength}
    return wordsByLength
    
def getWordsOfLengthN(n: int) -> list[str]:
    words = getAllWords()
    wordsByLength = sortWords(words)
    return wordsByLength[n]
    
    
if __name__ == "__main__":
    print(getWordsOfLengthN(28))