# https://inventwithpython.com/cracking/chapter7.html


def main():
    mymessage = 'Common sense is not so common.'
    mykey = 8
    ciphertext = encryptmessage(mykey, mymessage)
    print(ciphertext)


def encryptmessage(key, message):
    ciphertext = [''] * key
    for column in range(key):
        currentindex = column
        while currentindex < len(message):
            ciphertext[column] += message[currentindex]
            currentindex += key
    return ''.join(ciphertext)


if __name__ == '__main__':
    main()
