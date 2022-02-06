from advanced_fns import table_m2

"""
Write a program that reads an integer and displays all its smallest factors, also known as prime factors. For example, 
if the input integer is 120, the output should be as follows:
2, 2, 2, 3, 5
"""
# def is_prime(num):
#    for x in range(2, num):
#       if num % x == 0:
#          return False
#    return True
#
# def primes(num):
#    lst = []
#    for x in range(2, num):
#       if is_prime(x):
#          lst.append(x)
#    return lst
#
# def factors(num):
#    all_primes = primes(num)
#    factors_lst = []
#    for x in all_primes:
#       while num % x == 0:
#          factors_lst.append(x)
#          num //= x
#    return factors_lst

if __name__ == '__main__':

   table_m2()