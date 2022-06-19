import math

class Fraction:
    def __init__(self, numerator, denominator):
        gcd = math.gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __repr__(self):
        return "{}/{}".format(self.numerator, self.denominator)

    def __add__(self, other):
        lcm = math.lcm(self.denominator, other.denominator)
        return Fraction(self.numerator * (lcm // self.denominator) + other.numerator * (lcm // other.denominator), lcm)

    def __sub__(self, other):
        lcm = math.lcm(self.denominator, other.denominator)
        return Fraction(self.numerator * (lcm // self.denominator) - other.numerator * (lcm // other.denominator), lcm)

    def __iadd__(self, other):
        return self + other

    def __isub__(self, other):
        return self - other