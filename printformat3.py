__author__ = 'yuy001'

a = 3.1416
b = 5.6789

c = '{}'.format(a)
d = '{0:}'.format(a)
e = '{0:.3f}'.format(a)
f = '{:.2f}'.format(a)
g = '{0:.3f}'.format(a, b)
h = '{1:.2f} and {0:.3f}'.format(a, b)
i = '{:+.2f}'.format(a)

print c
print d
print e
print f
print g
print h
print i