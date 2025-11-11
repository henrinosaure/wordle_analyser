from wordslist import full_words_list, filtered_list
from wordle_functions import find_possible_words
from math import log2

color_permutations = ['ggggg', 'ggggb', 'ggggy', 'gggbg', 'gggbb', 'gggby', 'gggyg', 'gggyb', 'gggyy', 'ggbgg', 'ggbgb', 'ggbgy', 'ggbbg', 'ggbbb', 'ggbby', 'ggbyg', 'ggbyb', 'ggbyy', 'ggygg', 'ggygb', 'ggygy', 'ggybg', 'ggybb', 'ggyby', 'ggyyg', 'ggyyb', 'ggyyy', 'gbggg', 'gbggb', 'gbggy', 'gbgbg', 'gbgbb', 'gbgby', 'gbgyg', 'gbgyb', 'gbgyy', 'gbbgg', 'gbbgb', 'gbbgy', 'gbbbg', 'gbbbb', 'gbbby', 'gbbyg', 'gbbyb', 'gbbyy', 'gbygg', 'gbygb', 'gbygy', 'gbybg', 'gbybb', 'gbyby', 'gbyyg', 'gbyyb', 'gbyyy', 'gyggg', 'gyggb', 'gyggy', 'gygbg', 'gygbb', 'gygby', 'gygyg', 'gygyb', 'gygyy', 'gybgg', 'gybgb', 'gybgy', 'gybbg', 'gybbb', 'gybby', 'gybyg', 'gybyb', 'gybyy', 'gyygg', 'gyygb', 'gyygy', 'gyybg', 'gyybb', 'gyyby', 'gyyyg', 'gyyyb', 'gyyyy', 'bgggg', 'bgggb', 'bgggy', 'bggbg', 'bggbb', 'bggby', 'bggyg', 'bggyb', 'bggyy', 'bgbgg', 'bgbgb', 'bgbgy', 'bgbbg', 'bgbbb', 'bgbby', 'bgbyg', 'bgbyb', 'bgbyy', 'bgygg', 'bgygb', 'bgygy', 'bgybg', 'bgybb', 'bgyby', 'bgyyg', 'bgyyb', 'bgyyy', 'bbggg', 'bbggb', 'bbggy', 'bbgbg', 'bbgbb', 'bbgby', 'bbgyg', 'bbgyb', 'bbgyy', 'bbbgg', 'bbbgb', 'bbbgy', 'bbbbg', 'bbbbb', 'bbbby', 'bbbyg', 'bbbyb', 'bbbyy', 'bbygg', 'bbygb', 'bbygy', 'bbybg', 'bbybb', 'bbyby', 'bbyyg', 'bbyyb', 'bbyyy', 'byggg', 'byggb', 'byggy', 'bygbg', 'bygbb', 'bygby', 'bygyg', 'bygyb', 'bygyy', 'bybgg', 'bybgb', 'bybgy', 'bybbg', 'bybbb', 'bybby', 'bybyg', 'bybyb', 'bybyy', 'byygg', 'byygb', 'byygy', 'byybg', 'byybb', 'byyby', 'byyyg', 'byyyb', 'byyyy', 'ygggg', 'ygggb', 'ygggy', 'yggbg', 'yggbb', 'yggby', 'yggyg', 'yggyb', 'yggyy', 'ygbgg', 'ygbgb', 'ygbgy', 'ygbbg', 'ygbbb', 'ygbby', 'ygbyg', 'ygbyb', 'ygbyy', 'ygygg', 'ygygb', 'ygygy', 'ygybg', 'ygybb', 'ygyby', 'ygyyg', 'ygyyb', 'ygyyy', 'ybggg', 'ybggb', 'ybggy', 'ybgbg', 'ybgbb', 'ybgby', 'ybgyg', 'ybgyb', 'ybgyy', 'ybbgg', 'ybbgb', 'ybbgy', 'ybbbg', 'ybbbb', 'ybbby', 'ybbyg', 'ybbyb', 'ybbyy', 'ybygg', 'ybygb', 'ybygy', 'ybybg', 'ybybb', 'ybyby', 'ybyyg', 'ybyyb', 'ybyyy', 'yyggg', 'yyggb', 'yyggy', 'yygbg', 'yygbb', 'yygby', 'yygyg', 'yygyb', 'yygyy', 'yybgg', 'yybgb', 'yybgy', 'yybbg', 'yybbb', 'yybby', 'yybyg', 'yybyb', 'yybyy', 'yyygg', 'yyygb', 'yyygy', 'yyybg', 'yyybb', 'yyyby', 'yyyyg', 'yyyyb', 'yyyyy']

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
    attempt = attempt.lower()
    answer = answer.lower()

    result = ['b'] * len(attempt)

    # Count available letters in answer (will decrease as we match them)
    answer_counts = {}
    for char in answer:
        answer_counts[char] = answer_counts.get(char, 0) + 1

    # First pass: mark greens and decrease available counts
    for i in range(len(attempt)):
        if attempt[i] == answer[i]:
            result[i] = 'g'
            answer_counts[attempt[i]] -= 1

    # Second pass: mark yellows from remaining available letters
    for i in range(len(attempt)):
        if result[i] == 'b':  # Only check non-green positions
            if attempt[i] in answer_counts and answer_counts[attempt[i]] > 0:
                result[i] = 'y'
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


"""TO CHANGE: I REMOVED FULL_WORDS_LIST AND CHANGED IT FOR FILTERED LIST FOR A FASTER EXPERIENCE"""


def best_word_finder(bank):
    best_word=""
    best_word_bits=0
    for attempt in full_words_list:
        if best_word=="":
            best_word=attempt
            best_word_bits=average_bits(attempt, bank)
        elif best_word_bits<average_bits(attempt, bank):
            best_word = attempt
            best_word_bits = average_bits(attempt, bank)
    return {best_word:best_word_bits}




