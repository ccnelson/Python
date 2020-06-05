# https://inventwithpython.com/cracking/chapter11.html
# (There must be a "dictionary.txt" file in this directory)

UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'


def loaddictionary():
    dictionaryfile = open('dictionary.txt')
    englishwords = {}
    for word in dictionaryfile.read().split('\n'):
        englishwords[word] = None
    dictionaryfile.close()
    return englishwords


ENGLISH_WORDS = loaddictionary()


def getenglishcount(message):
    message = message.upper()
    message = removenonletters(message)
    possiblewords = message.split()
    if not possiblewords:
        return 0.0  # No words at all, so return 0.0
    matches = 0
    for word in possiblewords:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches) / len(possiblewords)


def removenonletters(message):
    lettersonly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersonly.append(symbol)
    return ''.join(lettersonly)


def isenglish(message, wordpercentage=20, letterpercentage=85):
    # By default, 20% of the words must exist in the dictionary file, and
    # 85% of all the characters in the message must be letters or spaces
    # (not punctuation or numbers).
    wordsmatch = getenglishcount(message) * 100 >= wordpercentage
    numletters = len(removenonletters(message))
    messageletterspercentage = float(numletters) / len(message) * 100
    lettersmatch = messageletterspercentage >= letterpercentage
    return wordsmatch and lettersmatch


print(isenglish('super'))
