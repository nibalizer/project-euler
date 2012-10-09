#!/opt/local/bin/python

"""
Project Euler
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

import math


number = 600851475143
#number = 13195
#number = 202020202
max_prime = 1

def is_prime(number):
    """
    returns true if the number is prime
    """
    global max_prime
    if number < max_prime:
        return False
#    print number
    #for i in xrange(2,int(math.sqrt(number)+1)):
    for i in xrange(2,number):
        if number % i == 0:
            return False
    max_prime = number
    return True

def is_whole(number):
    """
    returns ture if the number is a whole number
    """
    if number % 1 == 0:
        return True
    else:
        return False

#line used to test is_prime
#print map(is_prime, [9,10,11,12,13])
#line used to test is_whole
#print map(is_whole, [2,2.5, 10.01, 10.00])


prime_factors = []
for i in xrange(2,int(math.sqrt(number)+1)):
    quotient = number / float(i)
    if i % 10000 == 0:
        print i, quotient
    if is_whole(quotient):
        if is_prime(i):
            prime_factors.append(i)
            for prime in prime_factors:
                print prime,
            

print max(prime_factors)






