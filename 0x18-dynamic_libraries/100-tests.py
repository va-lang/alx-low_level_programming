import random
import ctypes

cops = ctypes.CDLL('./100-operations.so')

a = random.randint(-111, 111)
b = random.randint(-111, 111)

print("{} + {} = {}".format(a, b, cops.cop_add(a, b)))
print("{} - {} = {}".format(a, b, cops.cop_sub(a, b)))
print("{} x {} = {}".format(a, b, cops.cop_mul(a, b)))
print("{} / {} = {}".format(a, b, cops.cop_div(a, b)))
print("{} % {} = {}".format(a, b, cops.cop_mod(a, b)))
