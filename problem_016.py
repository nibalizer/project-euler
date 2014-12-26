#!/opt/local/bin/python
# vim: set fileencoding=utf-8 :

"""
Project Euler
Problem 16

Power digit sum
Problem 16

2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?


"""


a = 2**1000
print a
a = str(a)
sum_of = 0
for i in range(len(str(a))):
    sum_of += int(a[i])


print sum_of



