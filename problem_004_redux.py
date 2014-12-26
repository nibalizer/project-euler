#!/usr/bin/python

max_num = 0

for a in xrange(100, 999):
    for b in xrange(100, 999):
        #print a, b
        x = a * b
        str_x  = str(x)
        if str_x[:3] == str_x[3:][::-1]:
            if x > max_num:
                max_num = x


print max_num



