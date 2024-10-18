# Project: Wordle-N Optimization
# visualizeWordle.py
# visualize word scores from wordOptimization.py
# Created / Modified by: Mason Lee

import matplotlib.pyplot as plt
from organizeData import sortWords, getAllWords
    
"""This function generates a bar chart displaying the word length distribution for the
Scrabble Dictionary dataset"""
def visualizeWordDistribution():
    # Getting data
    wordLens = sortWords(getAllWords())
    lengths = [str(x) for x in wordLens.keys()]
    numWords = [len(x) for x in wordLens.values()]
    
    # Create plot
    fig, ax = plt.subplots(figsize=(10, 7))
    
    # Create bars
    ax.bar(lengths, numWords, color='xkcd:azure', edgecolor='black', linewidth=1)
    
    # Set tick sizes add title, and axis labels 
    ax.tick_params(axis='both', labelsize=14, pad=5)
    ax.set_title('Scrabble Dictionary Word Length Distribution', fontsize=20)
    ax.set_xlabel('Length of Words', fontsize=16)
    ax.set_ylabel('Number of Words', fontsize=16)
    
    # Rotating xticks
    plt.xticks(lengths, rotation=90)
    

if __name__ == "__main__":
    visualizeWordDistribution()
    
    