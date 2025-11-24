import sys

def add(a, b):
    return a + b

if _name_ == "_main_":
    x = eval(sys.argv[1])
    y = eval(sys.argv[2])
    print("sum:", add(x, y))
