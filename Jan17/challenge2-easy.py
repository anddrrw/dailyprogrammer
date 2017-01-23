"""
Reddit r/dailyprogrammer
Challenge: 2
Level: Easy
Date: 2017-01-22
Original Date of Challenge: 2012-02-10
Link: https://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_2/
Text:
Hello, coders! An important part of programming is being able to apply your programs, so your challenge for today is to
create a calculator application that has use in your life. It might be an interest calculator, or it might be something
that you can use in the classroom. For example, if you were in physics class, you might want to make a F = M * A calc.
EXTRA CREDIT: make the calculator have multiple functions! Not only should it be able to calculate F = M * A, but also
A = F/M, and M = F/A!
"""

class SquareCalculator:
    def __init__(self, length=-1, width=-1, area=-1):
        self.length = length
        self.width = width
        self.area = area

    def calc_area(self):
        if self.length == -1 or self.width == -1:
            return -1.0, 'Must know length and width to calculate area.'
        return float(self.length * self.width), None

    def calc_width(self):
        if self.length == -1 or self.area == -1:
            return -1.0, 'Must know length and area to calculate width.'
        return float(self.area / self.length), None

    def calc_length(self):
        if self.area == -1 or self.width == -1:
            return -1.0, 'Must know area and width to calculate length.'
        return float(self.area / self.width), None


def main():
    c1 = SquareCalculator(length=25, width=4)
    c2 = SquareCalculator(length=324, area=11)
    c3 = SquareCalculator()

    print c1.calc_area()[0]
    print c2.calc_width()[0]
    print c2.calc_length()[0]
    print c3.calc_area()[0]
    c3.length = 86
    c3.width = 22
    print c3.calc_area()[0]


if __name__ == '__main__':
    main()