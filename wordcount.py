#! /usr/bin/env python

items = " this is a test this is a test this is this this is a test this the quick brown fox jumps over the lazy dog under the bridge. twinkle twinkle little star how I wonder what you are. Queen and King of Hearts, this is the king and Queen of spades "


"""
# replace . with space
items  = items.replace(".", " ")
# take out left and right space
b = a.strip(" ")
# take out left space
c = b.lstrip(" ")
print(c)
# take out remaining space
d  = c.split(" ")
print(d)
"""


# replace . with space
items = items.replace(".", " ")

# replace to lowercase

items = items.lower()

## 
#To remove all whitespace characters (space, tab, newline, and so on) you can use split then join:
items = ' '.join(items.split())
items = items.split(" ")
print( items )

# count and put in dictionary
counts = dict()
for i in items:
  counts[i] = counts.get(i, 0) + 1

#print counts
# sort out from counts in decreasing order
for w in sorted(counts, key=counts.get, reverse=True):
#  print w, d[w]
   print w, counts[w] 

