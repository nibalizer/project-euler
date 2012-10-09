#!/opt/local/bin/python
# vim: set fileencoding=utf-8 :

"""
Project Euler
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

#Sieve of Eratosthenes

numbers_to_two_mil = xrange(2,2000000)

numerals = {}
primes = []

for i in numbers_to_two_mil:
    if i in numerals:
        continue
    if i not in numerals:
        primes.append(i)
        for unprime in xrange(i,2000000,i):
            numerals[unprime] = False


print primes
print sum(primes)


