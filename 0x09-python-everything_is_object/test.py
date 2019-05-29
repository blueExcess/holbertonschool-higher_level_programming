#!/usr/bin/python3
a = 'hbtn'
b = 'hbtn'
ida = id(a)
idb = id(b)
del a
del b
c = 'hbtn'
idc = id(c)
print(ida, idb, idc)
if ida == idb == idc:
    print("True")
