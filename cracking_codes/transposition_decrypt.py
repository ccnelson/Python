# https://inventwithpython.com/cracking/chapter8.html
import math


def main():
    mymessage = 'Cenoonommstmme oo snnio. s s c'
    mykey = 8
    plaintext = decryptmessage(mykey, mymessage)
    print(plaintext)


def decryptmessage(key, message):
    numofcolumns = int(math.ceil(len(message) / float(key)))
    numofrows = key
    numofshadedboxes = (numofcolumns * numofrows) - len(message)
    plaintext = [''] * numofcolumns
    column = 0
    row = 0
    for symbol in message:
        plaintext[column] += symbol
        column += 1 # Point to the next column.
        if (column == numofcolumns) or (column == numofcolumns - 1 and row >= numofrows - numofshadedboxes):
            column = 0
            row += 1
    return ''.join(plaintext)


if __name__ == '__main__':
    main()