import math


class Fraction:
    def __init__(self, numerator, denominator):
        gcd = math.gcd(numerator, denominator)
        self.den = denominator // gcd
        self.num = numerator // gcd

    def __str__(self):
        return "{0}/{1}".format(self.num, self.den)

    def __eq__(self, other):
        return self.num == other.num and self.den == other.den

    def __add__(self, other):
        lcm = math.lcm(self.num, self.den)
        new_num= self.num * lcm // self.den + other.num * lcm // other.den
        return Fraction(new_num, lcm)

    def __sub__(self, other):
        lcm = math.lcm(self.num, self.den)
        new_num = self.num * lcm // self.den - other.num * lcm // other.den
        return Fraction(new_num, lcm)

    def __iadd__(self, other):
        lcm = math.lcm(self.num, self.den)
        new_num = self.num * lcm // self.den + other.num * lcm // other.den
        return Fraction(new_num, lcm)




