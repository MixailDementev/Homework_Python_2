# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей. Для проверки своего кода используйте модуль fractions.
import math
from fractions import Fraction
from math import gcd

# a, b = map(int, input("Enter first fraction (in the form a/b): ").split("/"))
# c, d = map(int, input("Enter second fraction (in the form a/b): ").split("/"))


a1, b1 = map(int, input("Enter first fraction (in the form a/b): ").split("/"))
a2, b2 = map(int, input("Enter second fraction (in the form a/b): ").split("/"))


def sum_of_fractions():
    if b1 == b2:
        print("{}/{}".format(a1 + a2, b1))
    else:
        cd = int(b1 * b2 / gcd(b1, b2))
        rn = int(cd / b1 * a1 + cd / b2 * a2)
        g = gcd(rn, cd)
        n = int(rn / g)
        d = int(cd / g)
        print(f"Sum of fractions = " + "{}/{}".format(n, d) if n != d else n)


def multiplication_of_fractions():
    cd = int(b1 * b2)
    rn = int(a1 * a2)
    g2 = gcd(rn, cd)
    n = int(rn / g2)
    d = int(cd / g2)
    print(f"Product of fractions = " + "{}/{}".format(n, d) if n != d else n)


sum_of_fractions()
multiplication_of_fractions()

# Проверка
frac1_str = input("Enter first fraction (in the form a/b): ")
frac2_str = input("Enter second fraction (in the form a/b): ")

frac1 = Fraction(frac1_str)
frac2 = Fraction(frac2_str)

sum_frac = frac1 + frac2
prod_frac = frac1 * frac2

print("Sum of fractions:", sum_frac)
print("Product of fractions:", prod_frac)
