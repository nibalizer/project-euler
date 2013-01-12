#!/opt/local/bin/python
# vim: set fileencoding=utf-8 :

"""
Project Euler
Problem 012

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

           z: 12,2,,3,3,5,4,5,6,6,
 bigeerthanz: 12, 23,,5 ,6 

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?

"""


def triangle(x):
    return sum(xrange(x+1))

def divisors(x):
    divs = set()
    xf = float(x)
    for i in xrange(1, int(x/2)):
        #debug
        #print x, i, x/i
        if (xf / i) % 1 == 0:
           divs.add(i)
           divs.add(x/i)
    return sorted(divs)





#print triangle numbers like in example
for i in xrange(20):
    tri = triangle(i)
    print "{0}: {1}".format(tri, ",".join(map(str,divisors(tri))))

#print divisors(10)

num_divisors = 0

i = 0
while num_divisors < 500:
    i += 1
    tri = triangle(i)
    div = divisors(tri)
    len_div = len(div)
    print "{0}: {1}: {2}".format(tri, len_div, ",".join(map(str,div)))
    if len_div > num_divisors:
        num_divisors = len_div
    
    
#63748986 higher than 

