#!/usr/bin/python

"""
Project Euler
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def nat_num(biggest, factors):
    """
    Return a list of natural numbers below biggest that are divisible by one or
    more of the numbers in array factors. 
    """
    num = 0
    while num < biggest:
        for factor in factors:
            if num % factor == 0:
                yield num
                break
        num += 1
    
#for i in nat_num(1000, [3,5]):
#    print i,

print sum(nat_num(1000, [3,5]))
