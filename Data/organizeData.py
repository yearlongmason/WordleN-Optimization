# Project: Wordle-N Optimization
# organizeData
# Grab data from english.xlsx and sort into different text files based on word length
# e.g. wordle6Data.txt would have all 6 letter words
# Created / Modified by: Mason Lee

import pandas as pd

"""This function grabs data from a csv and returns all words"""
def getAllWords(file: str):
    
    # Get data from csv
    data = pd.read_csv(file)
    
    # Get words as their own list
    words = list([str(x).lower() for x in data["character"]])
    
    return words
    
"""Sorts all words into their own files arranged by length"""
def sortWordsIntoFiles(words: list[str]):
    words = [word for word in words if len(word) > 1]
    wordsByLength = {}
    [wordsByLength.update({x:[]}) for x in range(2, 21)]
    
    # Loop through each word
    for word in words:
        
        # If the word's length does not exist in the dictionary, it is not being recorded
        if len(word) not in wordsByLength.keys():
            continue
        
        # If it does exist, just add it to it's respective list
        wordsByLength[len(word)].append(word)
        
    # By the end of the loop we have a dictionary of lists formatted as:
    # {lengthOfWord : listOfAllWordsOfThatLength}
    
    # TODO: Add ability to write words to their respective files
    
    
if __name__ == "__main__":
    words = getAllWords("english.csv")
    sortWordsIntoFiles(words)