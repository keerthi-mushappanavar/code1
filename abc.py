import sys

def add(a, b):
    return a + b

if __name__ == "_main_":
    x = eval(sys.argv[1])
    y = eval(sys.argv[2])
    print("sum:", add(x, y))
