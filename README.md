# WordleN-Optimization
This project consists of a bot that is able to find optimized starting words for Wordle-N. Wordle-N is essentially the same as Wordle, but with words of different sizes. This means you can play Wordle with 6-letter words instead of 5 (or any number “N” that has English words of that size). We used the clues that Wordle gives the player as a way to rule out certain words, and then used letter frequency analysis as a heuristic for the algorithm to search through words faster. We’ve used the A* algorithm to find a list of optimal starting words for different “N” values (something along the lines of optimal starting words for “Wordle-6”).

# How to run our program
## Step By Step Guide
1. Install the colorama and numpy packages for your IDE by either
   * Right clicking on the imports > context actions > install package ___.
   * File > Settings/Preferences > Project > Python Interpreter > Search for ___.
   * Run pip install ___.
2. Run wordOptimization.py
3. Select an option by typing the number you want and hitting enter:
   - 1 to find the optimal starting word
   - 2 to score of an individual word
   - 3 exit the program
   
| Optimized Starting Word | Individual Words Score   |
|-------------------------|--------------------------|
| 4. Enter a word length to use <br> - we recommend 20+, using 3 - 19 can take a long time to run |4. Enter the word you would like to score <br> - please verify it exists in our list first|
| 5. Enter the number of sample words to use <br> - we recommend between 5 and 10, with a max of 15 to see results within a couple of minutes | 5.Enter the number of sample words to use <br> - This takes significantly less time to run, so larger samples work |
| 6. The output is a list of words and their scores <br> - Score is how many guesses it took to find the goal word <br> - The lower the score the better| 6. The output is how the average number of guesses to solve the word.


## In-depth explanation and guide
To run this program, simply run wordOptimization.py. You will be prompted for the length word you would like to get scores for (This is the "N" value in Wordle-N i.e. if you want to get rankings of 6 letter words, enter 6). Then you will be asked for a sample size. Because of runtime limitations based on the number of words in the dataset, most of the time we have to use samples. In order to run in a reasonable amount of time, we recommend choosing a number around 5 or 10. Then, the program starts to run by testing each word of length "N" against every other word in the sample. When the program is done running, it will output a list of all words of length N and the average number of guesses it took for that word to get to the goal word (lower average guesses suggests a better starting word). Be careful when choosing word length, and sample size. Different length words (3-19) and sample sizes (15+) may lead to code that runs for a very long time. If you're looking to test output, try out word length 2, and sample size 5.

OUTDATED BUT THE ORIGINAL CONCEPT: If you would like to get the score of an individual word, comment out the beginning code of the main section in wordOptimization.py, uncomment the second half of the main, and run wordOptimization.py. You will be prompted for a word and sample size, and it will output the average number of guesses it takes for that word to reach the goal word

# Sources
- [Data Set (Scrabble Dictionary)](https://figshare.com/articles/dataset/Enable_Scrabble_Dictionary/7492499/2)
- [Letter Frequencies](https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html)
- [Wordle-N Inspiration](https://zlee1.github.io/wordle.html)
