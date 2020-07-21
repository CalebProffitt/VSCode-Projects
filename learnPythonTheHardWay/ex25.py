def breakWords(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sortWords(words):
    """Sorts the words."""
    return sorted(words)

def printFirstWords(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def printLastWords(words):
    """Prints the last word after poppin it off."""
    word = words.pop(-1)
    print(word)

def sortSentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = breakWords(sentence)
    return sortWords(words)

def printFirstAndLast(sentence):
    """Prints the first and last words of the sentence."""
    words = breakWords(sentence)
    printFirstWords(words)
    printLastWords(words)

def printFirstAndLastSorted(sentence):
    """Sorts the words then prints the first and last ones."""
    words = sortSentence(sentence)
    printFirstWords(words)
    printLastWords(words)