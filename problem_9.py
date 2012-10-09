#!/opt/local/bin/python
# vim: set fileencoding=utf-8 :

"""
Project Euler
Problem 9


A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.


"""

"""
math section:

a2 + b2 = c2
a + b + c = 1000

"""

for i in xrange(1000):
    print i 
    for j in xrange(1000):
        for k in xrange(1000):
            if i + j + k == 1000:
                if i < j and j < k:
                    if i**2 + j**2 == k**2:
                        print "winner!", 
                        print i, j, k
            
    
print i, j, k
#200 375 425

