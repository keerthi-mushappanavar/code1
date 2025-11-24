import sys
from abc import add

# Take values from command-line arguments
a1 = eval(sys.argv[1])
b1 = eval(sys.argv[2])
a2 = eval(sys.argv[3])
b2 = eval(sys.argv[4])
a3 = eval(sys.argv[5])
b3 = eval(sys.argv[6])

def test_add_positive_numbers():
    assert add(a1, b1) == eval(sys.argv[7])

def test_add_negative_numbers():
    assert add(a2, b2) == eval(sys.argv[8])

def test_add_zero():
    assert add(a3, b3) == eval(sys.argv[9])
