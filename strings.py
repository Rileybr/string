# Vigenére cipher By Brandon Riley
# 10/19/17
# Encodes and decodes the Vigenére cipher


def encode():
    """
    Encodes text using the Vigenére cipher
    Adds the numbers related to the key, and looping the key if the phrase is longer, to the number that matches the
    phrase and if it goes over 25 it starts over at 0. Then it finds the letter that corresponds to the number we get.
    :return:
    """
    phrase = input("Please enter text to be encoded:")
    key = input("Please enter the key string:")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encoded_phrase = ""  # to get a blank string
    phrase = phrase.lower()
    phrase = phrase.replace(" ", "")  # gets rid of spaces
    key = key.lower()
    key = key.replace(" ", "")  # gets rid of spaces
    for x in range(len(phrase)):
        encoded = ((alphabet.index(key[x % len(key)])) + (alphabet.index(phrase[x]))) % 26
        letter = alphabet[encoded]
        encoded_phrase += letter
    print(encoded_phrase)


def decode():
    """
    Decodes text using Vigenére cipher
    Subtracts the number that matches the phrase by the numbers related to the key, and looping the key if the phrase
    is longer. Then it finds the letter that corresponds to the number we get.
    :return:
    """
    encoded_phrase = input("Please enter text to be decoded:")
    key = input("Please enter the key string:")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    phrase = ""  # to get a blank string
    for x in range(len(encoded_phrase)):
        decoded = ((alphabet.index(encoded_phrase[x])) - (alphabet.index(key[x % len(key)])))
        letter = alphabet[decoded]
        phrase += letter
    print(phrase)


def main():
    while True:
        to_do = input("Press e to encode, d to decode or q to quit:")
        if to_do == "e":
            encode()
        elif to_do == "d":
            decode()
        elif to_do == "q":
            print("Thanks for playing. Have a great day!")
            break


main()
