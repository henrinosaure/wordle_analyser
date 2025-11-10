from wordslist import full_words_list, filtered_list
from wordle_functions import find_possible_words
top_10={}

color_permutations = ['ggggg', 'ggggb', 'ggggy', 'gggbg', 'gggbb', 'gggby', 'gggyg', 'gggyb', 'gggyy', 'ggbgg', 'ggbgb', 'ggbgy', 'ggbbg', 'ggbbb', 'ggbby', 'ggbyg', 'ggbyb', 'ggbyy', 'ggygg', 'ggygb', 'ggygy', 'ggybg', 'ggybb', 'ggyby', 'ggyyg', 'ggyyb', 'ggyyy', 'gbggg', 'gbggb', 'gbggy', 'gbgbg', 'gbgbb', 'gbgby', 'gbgyg', 'gbgyb', 'gbgyy', 'gbbgg', 'gbbgb', 'gbbgy', 'gbbbg', 'gbbbb', 'gbbby', 'gbbyg', 'gbbyb', 'gbbyy', 'gbygg', 'gbygb', 'gbygy', 'gbybg', 'gbybb', 'gbyby', 'gbyyg', 'gbyyb', 'gbyyy', 'gyggg', 'gyggb', 'gyggy', 'gygbg', 'gygbb', 'gygby', 'gygyg', 'gygyb', 'gygyy', 'gybgg', 'gybgb', 'gybgy', 'gybbg', 'gybbb', 'gybby', 'gybyg', 'gybyb', 'gybyy', 'gyygg', 'gyygb', 'gyygy', 'gyybg', 'gyybb', 'gyyby', 'gyyyg', 'gyyyb', 'gyyyy', 'bgggg', 'bgggb', 'bgggy', 'bggbg', 'bggbb', 'bggby', 'bggyg', 'bggyb', 'bggyy', 'bgbgg', 'bgbgb', 'bgbgy', 'bgbbg', 'bgbbb', 'bgbby', 'bgbyg', 'bgbyb', 'bgbyy', 'bgygg', 'bgygb', 'bgygy', 'bgybg', 'bgybb', 'bgyby', 'bgyyg', 'bgyyb', 'bgyyy', 'bbggg', 'bbggb', 'bbggy', 'bbgbg', 'bbgbb', 'bbgby', 'bbgyg', 'bbgyb', 'bbgyy', 'bbbgg', 'bbbgb', 'bbbgy', 'bbbbg', 'bbbbb', 'bbbby', 'bbbyg', 'bbbyb', 'bbbyy', 'bbygg', 'bbygb', 'bbygy', 'bbybg', 'bbybb', 'bbyby', 'bbyyg', 'bbyyb', 'bbyyy', 'byggg', 'byggb', 'byggy', 'bygbg', 'bygbb', 'bygby', 'bygyg', 'bygyb', 'bygyy', 'bybgg', 'bybgb', 'bybgy', 'bybbg', 'bybbb', 'bybby', 'bybyg', 'bybyb', 'bybyy', 'byygg', 'byygb', 'byygy', 'byybg', 'byybb', 'byyby', 'byyyg', 'byyyb', 'byyyy', 'ygggg', 'ygggb', 'ygggy', 'yggbg', 'yggbb', 'yggby', 'yggyg', 'yggyb', 'yggyy', 'ygbgg', 'ygbgb', 'ygbgy', 'ygbbg', 'ygbbb', 'ygbby', 'ygbyg', 'ygbyb', 'ygbyy', 'ygygg', 'ygygb', 'ygygy', 'ygybg', 'ygybb', 'ygyby', 'ygyyg', 'ygyyb', 'ygyyy', 'ybggg', 'ybggb', 'ybggy', 'ybgbg', 'ybgbb', 'ybgby', 'ybgyg', 'ybgyb', 'ybgyy', 'ybbgg', 'ybbgb', 'ybbgy', 'ybbbg', 'ybbbb', 'ybbby', 'ybbyg', 'ybbyb', 'ybbyy', 'ybygg', 'ybygb', 'ybygy', 'ybybg', 'ybybb', 'ybyby', 'ybyyg', 'ybyyb', 'ybyyy', 'yyggg', 'yyggb', 'yyggy', 'yygbg', 'yygbb', 'yygby', 'yygyg', 'yygyb', 'yygyy', 'yybgg', 'yybgb', 'yybgy', 'yybbg', 'yybbb', 'yybby', 'yybyg', 'yybyb', 'yybyy', 'yyygg', 'yyygb', 'yyygy', 'yyybg', 'yyybb', 'yyyby', 'yyyyg', 'yyyyb', 'yyyyy']

bank=["apple","salet","churn","party","tacky","steal","crate","crane"]
def determine_colors(attempt,answer):
    result = ['b'] * len(attempt)
    answer_chars = list(answer)

    # First pass: mark greens (correct position)
    for i in range(len(attempt)):
        if attempt[i] == answer[i]:
            result[i] = 'g'
            answer_chars[i] = None  # Mark as used

    # Second pass: mark yellows (wrong position)
    for i in range(len(attempt)):
        if result[i] == 'b' and attempt[i] in answer_chars:
            result[i] = 'y'
            # Remove first occurrence to handle duplicate letters correctly
            answer_chars[answer_chars.index(attempt[i])] = None

    return ''.join(result)

    # Test examples


if __name__ == "__main__":
    print(wordle_check("crane", "crate"))  # gggby
    print(wordle_check("steal", "stale"))  # gggby
    print(wordle_check("speed", "abide"))  # bbygg
    print(wordle_check("erase", "speed"))  # yyyyb
    print(wordle_check("arise", "raise"))  # ygggg
    print(wordle_check("mamma", "maxim"))  # gybbb


def probability_of_color_pattern(word, color, bank):
