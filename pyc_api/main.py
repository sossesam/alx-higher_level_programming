#!/usr/bin/python3
import ctypes
my_custom_lib = ctypes.PyDLL("libFunny.so")
my_custom_lib.print_it.argtypes = [ctypes.py_object]
my_custom_lib.print_it("love\n")

