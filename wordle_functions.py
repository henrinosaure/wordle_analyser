def find_green(colors):
    """ input : str of colors
    output : list of positions that are green as bool"""
    greens =[]
    for i in range(5):
        if colors[i] == "G":
            greens.append(True)
        else:
            greens.append(False)
    return greens

def find_yellow(colors):
    """ input : str of colors
    output : list of positions that are yellow as bool"""
    yellows =[]
    for i in range(5):
        if colors[i] == "Y":
            yellows.append(True)
        else:
            yellows.append(False)
    return yellows

def find_black(colors):
    """ input : str of colors
    output : list of positions that are black as bool"""
    blacks =[]
    for i in range(5):
        if colors[i] == "B":
            blacks.append(True)
        else:
            blacks.append(False)
    return blacks

def find_possible_word(attempt, colors, word):
    """input : attempt (str), colors(str), word(str)
    output:  True if possible word, False if impossible word"""
    greens=find_green(colors)
    yellows=find_yellow(colors)
    blacks=find_black(colors)
    #test green logic
    for i in range(5):
        if (greens[i] and attempt[i]!=word[i]):
                return False
        if (not greens[i] and attempt[i]==word[i]):
            return False

    #test yellow logic
    for i in range(5):
        if yellows[i]:
            letter=attempt[i]
            if letter not in word:
                return False
            if letter == word[i]:
                return False
    # Test black logic
    for i in range(5):
        if blacks[i]:
            letter = attempt[i]
            # Count how many times this letter appears with green/yellow
            green_yellow_count = sum(1 for j in range(5)
                                     if attempt[j] == letter and (greens[j] or yellows[j]))
            # Count how many times this letter appears in the candidate word
            word_count = word.count(letter)

            # If black, the word should have exactly as many of this letter
            # as we've seen in green/yellow positions (no more)
            if word_count != green_yellow_count:
                return False
    return True

def find_possible_words(attempt, colors, bank):
    """
    input: attempt(str), colors(str) and bank (list of 5 letter str)
    output: list of 5 letter str of possible answers
    """
    possible_words=[]
    for word in bank:
        if find_possible_word(attempt, colors, word):
            possible_words.append(word)
    return possible_words

