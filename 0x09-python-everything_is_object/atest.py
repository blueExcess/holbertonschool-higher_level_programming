#!/usr/bin/python3
a = 1024
b = 1024
print(id(a))
print(id(b))
del a
del b
c = 1024
print(id(c))
