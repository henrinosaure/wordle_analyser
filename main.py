import wordslist,wordle_functions
from wordle_functions import find_possible_words
from wordslist import filtered_list


for i in range(6):
    attempt1 = input(f"Attempt#{i+1}: ").upper()
    colors1= input("What are the colors for the attempt (example: gybbb) : ")
    if i ==0:
        remaining_words = find_possible_words(attempt1,colors1,filtered_list)
    else:
        remaining_words = find_possible_words(attempt1, colors1, remaining_words)
    print(f"The {len(remaining_words)} possible words are: {remaining_words}")


