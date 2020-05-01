"""
Reddit r/dailyprogrammer
Challenge: 383
Level: Easy
Date: 2020-04-30
Original Date of Challenge: 2020-03-09
Link: https://www.reddit.com/r/dailyprogrammer/comments/ffxabb/20200309_challenge_383_easy_necklace_matching/

Imagine a necklace with lettered beads that can slide along the string. Here's an example image. In this example, you
could take the N off NICOLE and slide it around to the other end to make ICOLEN. Do it again to get COLENI, and so on.
For the purpose of today's challenge, we'll say that the strings "nicole", "icolen", and "coleni" describe the same
necklace.

Generally, two strings describe the same necklace if you can remove some number of letters from the beginning of one,
attach them to the end in their original ordering, and get the other string. Reordering the letters in some other way
does not, in general, produce a string that describes the same necklace.

Write a function that returns whether two strings describe the same necklace.

Examples
same_necklace("nicole", "icolen") => true
same_necklace("nicole", "lenico") => true
same_necklace("nicole", "coneli") => false
same_necklace("aabaaaaabaab", "aabaabaabaaa") => true
same_necklace("abc", "cba") => false
same_necklace("xxyyy", "xxxyy") => false
same_necklace("xyxxz", "xxyxz") => false
same_necklace("x", "x") => true
same_necklace("x", "xx") => false
same_necklace("x", "") => false
same_necklace("", "") => true
"""

def generate_necklaces(name):
    necklaces = []
    modified = name
    for c in name:
        modified = modified[1:] + c
        necklaces.append(modified)
    return necklaces if necklaces else ['']


def main():
    userName = input('Enter name: ')
    userNeck = input('Enter necklace to check: ')
    print(userNeck.lower() in generate_necklaces(userName.lower()))
    return


if __name__ == '__main__':
    main()
