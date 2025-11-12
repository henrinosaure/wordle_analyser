from wordslist import full_words_list, filtered_list
from wordle_functions import find_possible_words
from math import log2

from functools import lru_cache

@lru_cache(maxsize=None)
def color_finder(attempt, answer):
    """
    Check a Wordle attempt against the answer and return color pattern.

    Args:
        attempt: The guessed word (5 letters)
        answer: The correct word (5 letters)

    Returns:
        A string of colors where:
        - 'g' = green (correct letter in correct position)
        - 'y' = yellow (correct letter in wrong position)
        - 'b' = black/gray (letter not in word)

    """

    result = ['b'] * len(attempt)

    # Count available letters in answer (will decrease as we match them)
    answer_counts = {}
    for char in answer:
        answer_counts[char] = answer_counts.get(char, 0) + 1

    # First pass: mark greens and decrease available counts
    for i in range(len(attempt)):
        if attempt[i] == answer[i]:
            result[i] = 'G'
            answer_counts[attempt[i]] -= 1

    # Second pass: mark yellows from remaining available letters
    for i in range(len(attempt)):
        if result[i] == 'B':  # Only check non-green positions
            if attempt[i] in answer_counts and answer_counts[attempt[i]] > 0:
                result[i] = 'Y'
                answer_counts[attempt[i]] -= 1

    return ''.join(result)


"""
Goal: use bank to determine probability of word having specific color pattern, doing the average of how much it divides the bank
How to know how much color pattern divides the bank: use bits = log2(len(bank)/len(find_possible_words(attempt, color, bank)))."""

def bits(attempt, color, bank):
    return log2(len(bank)/len(find_possible_words(attempt,color,bank)))


def color_probability(attempt,color,bank):
    """Return the probability of a certain color pattern being output from wordle after giving a guess, using a certain bank"""
    hits=0
    for i in range(len(bank)):
        if color_finder(attempt,bank[i])==color:
            hits+=1
    return hits/len(bank)

def possible_colors(attempt,bank):
    """returns all possible color permutations from an attempt within a bank"""
    poss_colors=[]
    for word in bank:
        color=color_finder(attempt,word)
        if color not in poss_colors:
            poss_colors.append(color)
    return poss_colors


def average_bits(attempt,bank):
    """From a bank of possible words and an attempt, uses a new list of possible colors the attempt can take, and creates
    a parallel list of the probability of the color multiplied by the amount of bits it provides. The list is then added
    together"""
    colors = possible_colors(attempt, bank)
    parallel_list=[]
    for color in colors:
        parallel_list.append(color_probability(attempt, color, bank)*bits(attempt,color, bank))
    avg_bits=0
    for unit in parallel_list:
        avg_bits+=unit
    return avg_bits


def best_word_finder(bank, loading=False, update_interval=250):
    best_word = ""
    best_word_bits = 0
    total_words = len(full_words_list)

    for index, attempt in enumerate(full_words_list):
        # Display loading progress at custom intervals if enabled
        if loading and (index + 1) % update_interval == 0:
            progress = (index + 1) / total_words * 100
            print(f"\rProgress: {progress:.1f}% ({index + 1}/{total_words})", end='', flush=True)

        if best_word == "":
            best_word = attempt
            best_word_bits = average_bits(attempt, bank)
        elif best_word_bits < average_bits(attempt, bank):
            best_word = attempt
            best_word_bits = average_bits(attempt, bank)

    # Print final progress and newline
    if loading:
        print(f"\rProgress: 100.0% ({total_words}/{total_words})")

    return {best_word: best_word_bits}


def determine_strategy(bank):
    if len(bank)>25:
        return ["eliminate"]
    for word in bank:
        if len(find_possible_words(word))<2:
            return ["attempt",word]
    else:
        return ["eliminate"]