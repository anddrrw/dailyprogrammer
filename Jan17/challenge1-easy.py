"""
Reddit r/dailyprogrammer
Challenge: 1
Level: Easy
Date: 2017-01-10
Original Date of Challenge: 2012-02-09
Link: https://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/
Text:
    create a program that will ask the users name, age, and reddit username. have it tell them the information back, in the format:
    your name is (blank), you are (blank) years old, and your username is (blank)
    for extra credit, have the program log this information in a file to be accessed later.
"""

def main():
    name = raw_input('Please enter your name: ')
    age = raw_input('Please enter your age: ')
    usr = raw_input('Please enter your reddit username: ')
    result -n
    print 'Your name is {}, you are {} years old, and your username is {}.'.format(name, age, usr)

if __name__ == '__main__':
    main()