def find_green(colors):
    """ input : str of colors
    output : list of positions that are green as bool"""
    greens =[]
    for i in range(5):
        if colors[i] == "g":
            greens.append(True)
        else:
            greens.append(False)
    return greens

def find_yellow(colors):
    """ input : str of colors
    output : list of positions that are yellow as bool"""
    yellows =[]
    for i in range(5):
        if colors[i] == "y":
            yellows.append(True)
        else:
            yellows.append(False)
    return yellows

def find_black(colors):
    """ input : str of colors
    output : list of positions that are black as bool"""
    blacks =[]
    for i in range(5):
        if colors[i] == "b":
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
    for i in range(5):
        if (greens[i] and attempt[i]!=word[i]):
                return False
        if (not greens[i] and attempt[i]==word[i]):
            return False

    for i in range(5):
        if yellows[i]:
            letter=attempt[i]
            if letter not in word:
                return False
            if letter == word[i]:
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



