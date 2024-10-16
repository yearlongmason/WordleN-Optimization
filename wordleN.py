# Project: Wordle-N Optimization
# wordleN.py
# Implement WordleN class to be able to play/simulate WordleN.
# Created / Modified by: Mason Lee, Alex Mayo

from organizeData import getWordsOfLengthN
import random

class WordleN:
    
    """The constructor should get the 'n' value, which is the number of characters
    a word can have for this game of Wordle 
    (e.g. if n = 6 then it should get a list of all 6-letter words)
    Letter frequency is from https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html"""
    def __init__(self, n: int):
        self.n = n
        self.getData(n)
        self.alphabet = {
            "e" : 26, "a" : 25, "r" : 24, "i" : 23, "o" : 22, "t" : 21, "n" : 20,
            "s" : 19, "l" : 18, "c" : 17, "u" : 16, "d" : 15, "p" : 14, "m" : 13,
            "h" : 12, "g" : 11, "b" : 10, "f" : 9, "y" : 8, "w" : 7, "k" : 6,
            "v" : 5, "x" : 4, "z" : 3, "j" : 2, "q" : 1
        }
        self.used_letters = []
        
    """Sets the start word"""
    def setStartWord(self, startWord: str):
        # If it's a valid start word, set self.startWord to passed in word
        if startWord.lower() in self.possibleWords:
            self.startWord = startWord.lower()
            return
        
        # If the passed in word is invalid, alert the user and do nothing else
        print("ERROR: Invalid start word, please choose a different one")
        
    """Sets the goal word"""
    def setGoalWord(self, goalWord: str):
        # If it's a valid start word, set self.startWord to passed in word
        if goalWord.lower() in self.possibleWords:
            self.goalWord = goalWord.lower()
            return
        
        # If the passed in word is invalid, alert the user and do nothing else
        print("ERROR: Invalid start word, please choose a different one")
        
    """This function gets all words of length n using getWordsOfLengthN function"""
    def getData(self, n) -> None:
        self.possibleWords = getWordsOfLengthN(n)
    
    """This function should choose a random word from self.possibleWords
    as the goal word (the word we're searching for) called self.goalWord"""
    def getRandomGoalWord(self) -> None:
        self.setGoalWord(self.possibleWords[random.randint(0, len(self.possibleWords) - 1)])
    
    """This function should give back clues about self.goalWord in a dictionary
    It should be formatted as index:'color' where the color is the clue Wordle 
    would give a player
    For instance:
    passed in word: "plane"
    goalWord:       "palms"
    Would return:
    {0:'green',1:'yellow',2:'yellow',3:'grey',4:'grey'}
    """
    def checkWord(self, word: str) -> dict[int, str]:
        clues: dict[int, str] = {}
        
        # Loop through each index in guessed word
        for i in range(len(word)):
            # Determine index color based on goalWord
            if word[i] == self.goalWord[i]:
                clues[i] = "green"
            elif word[i] in self.goalWord:
                clues[i] = "yellow"
            else:
                clues[i] = "grey"
                self.used_letters.append(word[i])
                
        return clues
            
    
    """The function will run through the list of possible words and remove any
    that cannot be the solution.For instance, if the first letter is known to
    be G, then all words without G as the first letter are removed from the
    possible words list"""
    def cleanup_list(self, word, word_results: dict[int, str]) -> None:
        for i in range(len(word)):
            result = word_results.get(i)
            if result == 'green':
                self.filter_green(i, word)
            elif result == 'yellow':
                self.filter_yellow(i, word)
            elif result == 'grey' or result == 'gray':
                self.filter_grey(i, word)

    def filter_green(self, position: int, word: str) -> None:
        new_list = []
        for i in self.possibleWords:
            #If letters at position match
            if i[position] == word[position]:
                new_list.append(i)
        self.possibleWords = new_list
    
    def filter_yellow(self, position: int, word: str) -> None:
        new_list = []
        for i in self.possibleWords:
            #If letter is in but the positions do not match
            if word[position] in i and i[position] != word[position]:
                new_list.append(i)
        self.possibleWords = new_list

    def filter_grey(self, position: int, word: str) -> None:
        new_list = []
        for i in self.possibleWords:
            if word[position] not in i:
                new_list.append(i)
        self.possibleWords = new_list

    """Instead of having a static letter frequency we can change the letter frequency
    based on what letters have been used. This will help ensure the frequency of letters
    is evenly distributed, and that lesser used letters can still be used when solving."""
    def letterFrequency(self):
        new_dict = {}
        frequency = len(self.alphabet) - len(self.used_letters)
        for i in self.alphabet.keys():
            if i not in self.used_letters:
                new_dict[i] = frequency
                frequency -= 1
        self.alphabet = new_dict
    
    """This function should return a score for the word that is passed in.
    This is calculated by adding the frequency of each letter in the word.
    Since the purpose is to eliminate as many letters as possible, duplicate letters
    are only counted once"""
    def generateHeuristic(self, word: str) -> int:
        used_letters = []
        heuristic = 0
        for i in word:
            if i in used_letters:
                continue
            else:
                value = self.alphabet[i]
                heuristic += value
                used_letters.append(i)
        return heuristic
    
    
if __name__ == "__main__":
    # TEST CODE GOES HERE
    test = WordleN(5)
    test.setStartWord("Grape")
    test.setGoalWord("First")
    #test.checkWord("grape")
    #print(test.letterFrequency)