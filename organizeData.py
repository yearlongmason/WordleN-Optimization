# Project: Wordle-N Optimization
# organizeData.py
# Grab data from scrabbleWords.csv and sort into different word length buckets
# Created / Modified by: Mason Lee

"""This function grabs data from a csv and returns all words"""
def getAllWords() -> dict[str, int]:
    
    # Get data from csv
    with open(file="Data/scrabbleWords.csv") as file:
        words = file.read()
        
    # Turn csv into just list of words
    words = words.split("\n")[1:]
    words = [str(word.split(",")[0]) for word in words if word.split(",")[0] != ""]
    
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
    
    #print(getAllWords())
    #print(getWordsOfLengthN(28))
    print(len(getWordsOfLengthN(24)))
    
    # Data visualization of word length distribution
    #import matplotlib.pyplot as plt
    #lenWords = [str(length) for length, words in sortWords(getAllWords()).items()]
    #numWords = [len(words) for length, words in sortWords(getAllWords()).items()]
    #plt.figure(figsize=(10,6))
    #plt.bar(lenWords, numWords)