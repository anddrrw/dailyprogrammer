"""
Reddit r/dailyprogrammer
Challenge: 4
Level: Easy
Date: 2017-03-03
Actual Date (lol): 2020-04-30
Original Date of Challenge: 2012-12-12
Link: https://www.reddit.com/r/dailyprogrammer/comments/pm6oj/2122012_challenge_4_easy/
Text:
You're challenge for today is to create a random password generator!

For extra credit, allow the user to specify the amount of passwords to generate.

For even more extra credit, allow the user to specify the length of the strings he wants to generate!
"""
import random
import string


def main():
    length = random.randint(10, 100)
    password = ''
    for x in range(0, length):
        password += random.choice(string.ascii_letters + string.digits)
    print('Your password is: ' + password)


if __name__ == '__main__':
    main()