#!/usr/bin/env python
numbers = [1, 2, 3, 4, 5]
square = lambda x: x*x
squarenum = map(square, numbers)
print numbers
print squarenum
