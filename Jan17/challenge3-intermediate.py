"""
Reddit r/dailyprogrammer
Challenge: 3
Level: Intermediate
Date: 2017-01-25
Original Date of Challenge: 2012-02-11
Link: https://www.reddit.com/r/dailyprogrammer/comments/pkwb1/2112012_challenge_3_intermediate/
Text:
Welcome to cipher day!
Create a program that can take a piece of text and encrypt it with an alphabetical substitution cipher. This can ignore white space, numbers, and symbols.
for extra credit, make it encrypt whitespace, numbers, and symbols!
for extra extra credit, decode someone elses cipher!
"""
import argparse

def encrypt(lInt):
    """
    Subtract 5 from each ascii int, will loop back to 255.
    :param li: list of integers
    :return: encrypted string
    """
    encryptedList = []
    for num in lInt:
        num-=5
        if num < 0:
            num = 255 + num
        encryptedList.append(num)

    return ''.join(chr(i) for i in encryptedList)

def str_to_ascii(s):
    """
    Convert string to ascii
    :param s: string of text
    :return: list of chars in ascii ints
    """
    return [ord(c) for c in s]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('usrInput', help='String to encrypt.')
    args = parser.parse_args()
    ascii = str_to_ascii(args.usrInput)
    print encrypt(ascii)

if __name__ == '__main__':
    main()
