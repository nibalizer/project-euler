#!/opt/local/bin/python
# vim: set fileencoding=utf-8 :

"""
Project Euler
Problem NUMBER

Self powers
Problem 48

The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.



"""

sumof = 0

for i in range(1,1000):
    result = i**i
    r = str(result)[-10:]
    sumof += int(r)


print sumof
