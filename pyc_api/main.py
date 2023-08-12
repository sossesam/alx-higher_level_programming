#!/usr/bin/python3
import ctypes
my_custom_lib = ctypes.PyDLL("libFunny.so")
my_custom_lib.print_it.argtypes = [ctypes.c_char_p]
my_custom_lib.print_it.restype = ctypes.c_int
num = my_custom_lib.print_it(b"love\n")
print(num)
my_custom_lib.greet()
