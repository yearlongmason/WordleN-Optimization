# Project: Wordle-N Optimization
# wordleN.py
# Impliment WordleN class to be able to play/simulate WordleN.
# Created / Modified by: Mason Lee

class WordleN():
    
    """The constructor should get the 'n' value, which is the number of characters
    a word can have for this game of Wordle 
    (e.g. if n = 6 then it should get a list of all 6 letter words)"""
    def __init__(self, n: int, startWord: str):
        self.n = n
        self.startWord = startWord
        self.getData(n)
        self.chooseWord()
        
    """This function should grab data from the data folder and store all 
    words of length 'N' in a list called something like self.possibleWords"""
    def getData(self, n) -> None:
        pass
    
    """This function should choose a random word from self.possibleWords
    as the goal word (the word we're searching for) called self.goalWord"""
    def chooseWord(self) -> None:
        pass
    
    """This function should give back clues about the goal word in a dictionary
    It should be formatted as index:'color' 
    For instance:
    {0:'green',1:'yellow',2:'yellow',3:'grey',4:'grey'}
    We can then pass this to a separate function to eliminate words"""
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
    it would have a score of 5 because S and A are worth 2 and N is worth 1"""
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