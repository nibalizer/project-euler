#!/opt/local/bin/python
# vim: set fileencoding=utf-8 :

"""
Project Euler
Problem 4



A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.


"""


biggest = 0
for i in xrange(100,1000):
    for j in xrange(100,1000):
        num = i * j
        a, b = str(num)[:3], str(num)[3:][::-1]
        if a == b:
            if num > biggest:
                biggest = num

print biggest
