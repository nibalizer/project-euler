#!/opt/local/bin/python
# vim: set fileencoding=utf-8 :

"""
Project Euler
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

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

primes = []
a_number = 1

while len(primes) < 10002:
    if is_prime(a_number):
       primes.append(a_number)
    a_number += 1

print max(primes)

    
    
    
