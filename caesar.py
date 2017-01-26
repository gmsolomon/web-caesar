from sys import argv, exit
#from helpers import rotate_character


# this function returns the position of the (letter) in the alphabet
def alphabet_position(letter):
    letter_lower = letter.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet.find(letter_lower)


# this function rotates the character (char) the amount of (rot) to create an encrypted message
def rotate_character(char,rot):
    alphabet_low = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # this if statement determine if char is an upper or lower case letter.
    # It will return an encrypted upper case letter if the original char was upper case and
    # will return an encrypted lower case letter if the original char was lower case.
    # if the original char was neither an upper nor lower case letter, then it will
    # just return the orginal char without encrypting it
    if char in alphabet_low:
        position = alphabet_position(char) # calls function alphabet_position to return location of char
        new_position = (position + rot) % 26 # will change the character (char) by moving it (rot) places to the right in the alphabet
        return alphabet_low[new_position]  # returns encypted character
    elif char in alphabet_upper:
        position = alphabet_position(char) # calls function alphabet_position to return location of char
        new_position = (position + rot) % 26 # will change the character (char) by moving it (rot) places to the right in the alphabet
        return alphabet_upper[new_position] # returns encrypted character
    else:
        return char

def encrypt(text,rot):

    encrypted = ""
    for letter in text:
        new_let = rotate_character(letter,rot) # calls the function rotate_character
        encrypted = encrypted + new_let
    return encrypted
