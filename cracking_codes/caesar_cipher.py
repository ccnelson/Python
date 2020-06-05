# https://inventwithpython.com/cracking/chapter5.html

#message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'
message = 'This is my secret message.'
key = 13
mode = 'encrypt'  # Set to either 'encrypt' or 'decrypt'.
#mode = 'decrypt'  # Set to either 'encrypt' or 'decrypt'.
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)
        translatedIndex = None
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key
        # Handle wraparound
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)
        translated = translated + SYMBOLS[translatedIndex]
    else:
        # Append the symbol without encrypting/decrypting:
        translated = translated + symbol
# Output the translated string:
print(translated)

