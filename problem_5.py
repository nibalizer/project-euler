#!/opt/local/bin/python
# vim: set fileencoding=utf-8 :

"""
Project Euler
Problem 5


2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


"""

number = 1

while True:
    number += 1
    if number % 10000 == 0:
        print number
    for i in xrange(1,21):
        if not number % i == 0:
            break
    else:
        print "and the winner is: ",
        print number
        break


