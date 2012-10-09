#!/opt/local/bin/python


# a genreator that yields items instead of returning a list

def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1


print sum(firstn(1000000))
