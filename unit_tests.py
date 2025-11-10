from wordle_functions import find_possible_word, find_possible_words
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
    assert find_possible_word("salet", "bgggg", "salet") == False  # 's' black, but in word
    assert find_possible_word("salet", "bgggg", "tales") == False  # 's' black, but in word

    print("Test 2: Multiple black letters - none should appear")
    assert find_possible_word("salet", "bbggg", "mplet") == True  # 's','a' black, not in word
    assert find_possible_word("salet", "bbggg", "males") == False  # 'a' black, but in word
    assert find_possible_word("salet", "bbggg", "splet") == False  # 's' black, but in word

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

test_find_possible_word()