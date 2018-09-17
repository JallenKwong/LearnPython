from ctypes import *

#C的Union联合体在Python中定义


class barley_amount(Union):
    _fields_=[("barley_long", c_long),
              ("barley_int",c_int),
              ("barley_char", c_char * 8),
              ]

value = raw_input("Enter the amount of barley to put into the beer vat:")

my = barley_amount(int(value))

print "long: %ld" % my.barley_long
print "int: %d" % my.barley_int
print "char: %s" % my.barley_char
