import string
import random


def generateRandomStrings(length):
    i = 0
    randomString = ""
    while i < length:
        newString = random.choice(string.ascii_letters)
        randomString = randomString + newString
        i += 1
    return randomString
