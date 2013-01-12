#!/opt/local/bin/python
# vim: set fileencoding=utf-8 :

"""
Project Euler
Problem 014

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""


def collatz_length(x):
    num = x
    counter = 0
    while x > 1:
        if x % 2 == 0:
            x = x / 2
        else:
            x = (3 * x ) + 1
        counter += 1
    return counter

def collatz_length_verbose(x):
    num = x
    counter = 0
    while x > 1:
        print x,
        if x % 2 == 0:
            x = x / 2
        else:
            x = (3 * x ) + 1
        counter += 1
    print
    return counter


chain_length = 0
number = 0
for i in xrange(1, 1000001):
    length = collatz_length(i)
    if length > chain_length:
        chain_length = length
        number = i

print "longest chain is %s from number %s" % (chain_length,number)
print "chain is",
collatz_length_verbose(chain_length)











