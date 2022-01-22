import math


class Fraction:

  def __init__(self, numerator, denominator):
    gcd = math.gcd(numerator, denominator)
    self.numerator = numerator // gcd
    self.denominator = denominator // gcd

  def __str__(self):
    return "{0}/{1}".format(self.numerator, self.denominator)

  def __add__(self, other):


if __name__ == '__main__':
  f = Fraction(4, 8)
  print(f)


