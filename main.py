import wordslist,wordle_functions
from wordle_functions import find_possible_words
from wordslist import filtered_list
from optimal_finder import best_word_finder


for i in range(6):
    attempt1 = input(f"Attempt#{i+1}: ").upper()
    colors1= input("What are the colors for the attempt (example: gybbb) : ")
    if colors1=="ggggg":
        print("Congrats on your win choomba")
        break
    if i ==0:
        remaining_words = find_possible_words(attempt1,colors1,filtered_list)
    else:
        remaining_words = find_possible_words(attempt1, colors1, remaining_words)
    print(f"The {len(remaining_words)} possible words are: ")
    print(remaining_words)
    best_word = best_word_finder(remaining_words)
    if best_word=={"AAHED":0.0}:
        print(f"The best word to play is {remaining_words[0]}")
    else:
        print(f"the best word to play is {best_word_finder(remaining_words)}")

