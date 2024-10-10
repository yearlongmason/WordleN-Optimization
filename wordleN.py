# Project: Wordle-N Optimization
# wordleN.py
# Impliment WordleN class to be able to play/simulate WordleN.
# Created / Modified by: Mason Lee

from organizeData import getWordsOfLengthN
import random

class WordleN():
    
    """The constructor should get the 'n' value, which is the number of characters
    a word can have for this game of Wordle 
    (e.g. if n = 6 then it should get a list of all 6 letter words)"""
    def __init__(self, n: int):
        self.n = n
        self.getData(n)
        
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
        self.possibleWords = getWordsOfLengthN(self.n)
    
    """This function should choose a random word from self.possibleWords
    as the goal word (the word we're searching for) called self.goalWord"""
    def getRandomGoalWord(self) -> None:
        pass
    
    """This function should give back clues about self.goalWord in a dictionary
    It should be formatted as index:'color' where the color is the clue Wordle 
    would give a player
    For instance:
    passed in word: "plane"
    goalWord:       "palms"
    Would return:
    {0:'green',1:'yellow',2:'yellow',3:'grey',4:'grey'}
    We can then pass this to a separate function to eliminate words
    Remember: This should also support any words of length N"""
    def checkWord(self, word: str) -> dict[int, str]:
        pass
    
    """Instead of having a static letter frequency we can re-search all of the remaining 
    words in self.possibleWords and get the letter frequency of those words, and use that
    as the basis of a hueristic
    for instance if the remaining words are, Slug, Plan, and Slap, the frequencies would be:
    {L:3, S:2, P:2, A:2, U:1, G:1, N:1}
    We can then score each word by adding the frequency of each letter in the word
    For instance with these frequencies if we were to score the word: Scan
    it would have a score of 5 because S and A are worth 2 and N is worth 1"""
    @property
    def letterFrequency(self) -> dict[str, int]:
        pass
    
    """This function should return a score for the word that is passed in.
    Reusing the above example:
    if the remaining words are, Slug, Plan, and Slap, the frequencies would be:
    {L:3, S:2, P:2, A:2, U:1, G:1, N:1}
    We can then score each word by adding the frequency of each letter in the word
    For instance with these frequencies if we were to score the word: Scan
    it would have a score of 5 because S and A are worth 2 and N is worth 1
    This function should call letter frequency to get the remaining letter frequencies"""
    def generateHeuristic(self, word: str) -> int:
        pass
    
    """This function may need to contain other smaller functions to accomplish the goal
    The idea is for this function is to be able to use astar() to search for the goalWord.
    astar() will likely give back a node or a list of words that it took to reach the solution.
    Since astar returns the shortest path we will have to modify it to also return the explored nodes
    or the path it took to reach the word goal we know how many words it explored to get to the 
    goal word which will be the basis of how we determine how good a starting word is 
    (length of the list of explored nodes)
    So essentially this function will use astar() to somehow get a list of words
    it had to guess to reach the goal word"""
    def getSolutionPath(self) -> list[str]:
        pass
    
    
if __name__ == "__main__":
    # TEST CODE GOES HERE
    test = WordleN(5)
    test.setStartWord("Grape")
    test.setGoalWord("First")
    print(test.possibleWords)
    print(f"Start word: {test.startWord} \nGoal word: {test.goalWord}")