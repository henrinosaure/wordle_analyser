from wordle_functions import find_possible_word, find_possible_words
from optimal_finder import color_finder

def test_find_possible_word():
    print("Testing find_possible_word...")

    assert find_possible_word("salet","bbbbb","steak")==False
    print("Test 1 complete")
    assert find_possible_word("pleas", "ggggg", "pleak")==False
    print("Test 2 complete")
    assert find_possible_word("salet", "bybbb","appar")==True
    print("Test 3 complete")
    assert find_possible_word("salet","bbbbb", "churn")==True
    print("Test 4 complete")
    assert find_possible_word("salet", "ggggg", "salet")==True
    print("Test 5 complete")
    assert find_possible_word("salet", "yyyyy","alets")==True
    print("Test 6 complete")
    assert find_possible_word("salet", "ybyby","lotos")==True
    print("Test 7 complete")
    assert find_possible_word("ssspo", "yygbb","awsss")==True
    print("Test 8 complete")
    assert find_possible_word("ssspo", "yygbb","awsss")==True
    print("Test 9 complete")
    assert find_possible_word("salet", "yyyyy","aleks")==False
    print("Test 9 complete")
    assert find_possible_word("sally", "bbgbb", "pplpp")==True
    print("Test 10 complete")
    assert find_possible_word("salet", "bbbbb", "salet")==False
    print("Test 11 complete")
    assert find_possible_word("salet", "gybbb","steal")==False

    print("Tests for find_possible_word are complete")

bank=["apple", "cooch","toing","salet","bingl","crane","toast"]
def test_find_possible_words():
    print("Testing find_possible_words...")

    assert find_possible_words("salet","ggggg",bank)==["salet"]
    print("Test 1 complete")
    assert find_possible_words("salet","bbbbb",bank)==["cooch"]
    print("Test 2 complete")
    assert find_possible_words("crank","ggggb",bank)==["crane"]
    print("Test 3 complete")
    assert find_possible_words("salet","bbybb",bank)==["bingl"]
    print("Test 4 complete")
    assert find_possible_words("hhhhh","bbbbb",bank)==["apple","toing","salet","bingl","crane","toast"]
    print("Test 5 complete")
    assert find_possible_words("salet","bbggg",bank)==[]
    print("Test 6 complete")

def test_black():
    print("Test 1: Single black letter - should not appear anywhere in word")
    assert find_possible_word("salet", "bgggg", "palet") == True  # 's' black, not in word
    print("Test 1.1 complete")
    assert find_possible_word("salet", "bgggg", "salet") == False  # 's' black, but in word
    print("Test 1.2 complete")
    assert find_possible_word("salet", "bgggg", "tales") == False  # 's' black, but in word
    print("Test 1.3 complete")

    print("Test 2: Multiple black letters - none should appear")
    assert find_possible_word("salet", "bbggg", "mplet") == True  # 's','a' black, not in word
    print("Test 2.1 complete")
    assert find_possible_word("salet", "bbggg", "males") == False  # 'a' black, but in word
    print("Test 2.2 complete")
    assert find_possible_word("salet", "bbggg", "splet") == False  # 's' black, but in word
    print("Test 2.3 complete")

    print("Test 3: All black letters")
    assert find_possible_word("salet", "bbbbb", "truck") == True  # none of s,a,l,e,t in word
    assert find_possible_word("salet", "bbbbb", "style") == False  # has 's', 't', 'e', 'l'
    assert find_possible_word("salet", "bbbbb", "water") == False  # has 'a', 't', 'e'
    assert find_possible_word("salet", "bbbbb", "salty") == False  # has 's', 'a', 'l', 't'

    print("Test 4: Black letters in different positions")
    assert find_possible_word("salet", "gbgbg", "salad") == False  # 'a' black at pos 1, but appears at pos 1 in "salad"
    assert find_possible_word("salet", "gbgbg", "solid") == False  # 'l' black at pos 2, but in word
    assert find_possible_word("salet", "gggbg", "saler") == False  # 'e' black at pos 3, but in word

    print("Test 5: Black at end")
    assert find_possible_word("salet", "ggggb", "sales") == True  # 't' black, not in word
    assert find_possible_word("salet", "ggggb", "salet") == False  # 't' black, but in word

    print("Test 6: Black at beginning")
    assert find_possible_word("salet", "bgggg", "walet") == True  # 's' black, not in word
    assert find_possible_word("salet", "bgggg", "asset") == False  # 's' black, but appears in word

    print("Test 7: Alternating blacks and greens")
    assert find_possible_word("abcde", "bgbgb", "fgfhf") == False  # a,c,e black and not in word
    assert find_possible_word("abcde", "bgbgb", "fbche") == False  # 'c' black but in word
    assert find_possible_word("abcde", "bgbgb", "abede") == False  # 'a','e' black but in word

    print("Test 8: Black with repeated letters in attempt")
    assert find_possible_word("speed", "bbbbb", "cargo") == True  # s,p,e,e,d all black, none in word
    assert find_possible_word("speed", "bbbbb", "creep") == False  # 'e','p' black but in word
    assert find_possible_word("alley", "bbbbb", "truck") == True  # a,l,l,e,y all black, none in word
    assert find_possible_word("alley", "bbbbb", "elite") == False  # 'e','l' black but in word

    print("Test 9: Only blacks and yellows (no greens)")
    assert find_possible_word("salet", "ybbyb", "tests") == True  # 'a','l' black but 'l' in word
    assert find_possible_word("salet", "ybbyb", "noter") == False  # 's','t' yellow elsewhere, 'a','l' black not in word

    print("Test 10: Black letter that appears multiple times in word")
    assert find_possible_word("three", "bgbbb", "truck") == False  # h,r,e,e black, none in word
    assert find_possible_word("three", "bgbbb", "refer") == False  # 'r','e' black but appear in word
    assert find_possible_word("llama", "bbbbb", "trick") == True  # l,l,a,m,a black, none in word
    assert find_possible_word("llama", "bbbbb", "llama") == False  # all black but all in word

    print("All black logic tests passed!")


def test_color_finder():
    """Comprehensive tests for the color_finder function."""


    print("Test 1: All letters correct")
    assert color_finder("crate", "crate") == "ggggg"
    print("Test 1.1 complete")
    assert color_finder("hello", "hello") == "ggggg"
    print("Test 1.2 complete")
    assert color_finder("WORLD", "world") == "ggggg"  # Case insensitive
    print("Test 1.3 complete")

    print("\nTest 2: No matching letters")
    assert color_finder("abcde", "fghij") == "bbbbb"
    print("Test 2.1 complete")
    assert color_finder("think", "jumpy") == "bbbbb"
    print("Test 2.2 complete")
    assert color_finder("crane", "thumb") == "bbbbb"
    print("Test 2.3 complete")

    print("\nTest 3: All letters present but wrong positions")
    assert color_finder("abcde", "edbca") == "yyyyy"
    print("Test 3.1 complete")
    assert color_finder("steam", "mates") == "yyyyy"
    print("Test 3.2 complete")

    print("\nTest 4: Mixed green, yellow, black")
    assert color_finder("crane", "crate") == "gggbg"
    print("Test 4.1 complete")
    assert color_finder("steal", "stale") == "ggyyy"
    print("Test 4.2 complete")
    assert color_finder("arise", "raise") == "yyggg"
    print("Test 4.3 complete")
    assert color_finder("crime", "prime") == "bgggg"
    print("Test 4.4 complete")

    print("\nTest 5: Duplicate letters in attempt")
    print("Test 5.1: Two e's in answer, two in attempt at correct positions")
    assert color_finder("speed", "abide") == "bbyby"
    print("Test 5.1 complete")

    print("Test 5.2: Two e's in answer, two in attempt at wrong positions")
    assert color_finder("erase", "speed") == "ybbyy"
    print("Test 5.2 complete")

    print("Test 5.3: Two m's in answer, three m's in attempt")
    assert color_finder("mamma", "maxim") == "ggybb"  # 1st m green, 2nd m yellow, 3rd m black
    print("Test 5.3 complete")

    print("Test 5.4: One a in answer, three a's in attempt (a at position 0)")
    assert color_finder("aaaaa", "abcde") == "gbbbb"
    print("Test 5.4 complete")

    print("Test 5.5: One a in answer, three a's in attempt (a at position 3)")
    assert color_finder("aapap", "bcade") == "ybbbb"
    print("Test 5.5 complete")

    print("\nTest 6: Duplicate letters in answer")
    print("Test 6.1: Two e's in answer, one e in attempt (correct position)")
    assert color_finder("crane", "geese") == "bbbbg"
    print("Test 6.1 complete")

    print("Test 6.2: Two o's in answer, two o's in attempt (different positions)")
    assert color_finder("robot", "floor") == "yybgb"
    print("Test 6.2 complete")

    print("Test 6.3: Three e's in answer, one e in attempt")
    assert color_finder("crane", "eeeee") == "bbbbg"
    print("Test 6.3 complete")

    print("\nTest 7: Case insensitivity")
    assert color_finder("CRANE", "crate") == "gggbg"
    print("Test 7.1 complete")
    assert color_finder("Crane", "CRATE") == "gggbg"
    print("Test 7.2 complete")
    assert color_finder("CrAnE", "CrAtE") == "gggbg"
    print("Test 7.3 complete")


    print("\nTest 9: Edge cases")
    print("Test 9.1: Letter appears once in answer, twice in attempt (one correct position)")
    assert color_finder("poppy", "promo") == "gybbb"  # p green at 0, second p black, third p yellow
    print("Test 9.1 complete")

    print("Test 9.2: Letter appears twice in answer, once in attempt (wrong position)")
    assert color_finder("great", "eerie") == "byybb"
    print("Test 9.2 complete")

    print("Test 9.3: All same letter in attempt, one match in answer")
    assert color_finder("lllll", "hello") == "bbggb"
    print("Test 9.3 complete")

    print("All tests complete")

