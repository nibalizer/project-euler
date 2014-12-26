#!/opt/local/bin/python
# vim: set fileencoding=utf-8 :

"""
Project Euler
Problem 17


Number letter counts
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

"""

highest_num = 5

import num2word
import re


count = 0
for num in range(1, 1000+1):
    a = re.sub('[ -]', '', num2word.to_card(num))
    print a
    count += len(a)


print count
