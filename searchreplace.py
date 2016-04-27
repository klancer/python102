#! /usr/bin/env python


"""
in = open('path/to/input/file').read()
out = open('path/to/input/file', 'w')
replacements = {'zero':'0', 'temp':'bob', 'garbage':'nothing'}
for i in replacements.keys():
    in = in.replace(i, replacements[i])
out.write(in)
out.close
"""
words = "this is a zero test temp and garbage garbage temp and zero is a zero"
print( words )

replacements = {'zero':'0', 'temp':'bob', 'garbage':'nothing'}
for i in replacements.keys():
    words = words.replace(i, replacements[i])

print( words )




