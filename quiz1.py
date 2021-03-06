# CS 61A Fall 2014
# Name:
# Login:


def two_equal(a, b, c):
    """Return whether exactly two of the arguments are equal and the
    third is not.

    >>> two_equal(1, 2, 3)
    False
    >>> two_equal(1, 2, 1)
    True
    >>> two_equal(1, 1, 1)
    False
    >>> result = two_equal(5, -1, -1) # return, don't print
    >>> result
    True

    """
    "*** YOUR CODE HERE ***"
    return (a == b) or (a == c) or (b == c) 

def same_hailstone(a, b):
    """Return whether a and b are both members of the same hailstone
    sequence.

    >>> same_hailstone(10, 16) # 10, 5, 16, 8, 4, 2, 1
    True
    >>> same_hailstone(16, 10) # order doesn't matter
    True
    >>> result = same_hailstone(3, 19) # return, don't print
    >>> result
    False

    """
    "*** YOUR CODE HERE ***"
    if a > b:
        small,big = b,a
    else:
        small,big = a,b
    result = False
    while big != 1:
        if (big % 2 == 0):
            big //= 2
        else:
            big = n1*3 + 1
    return steps
    


def near_golden(perimeter):
    """Return the integer height of a near-golden rectangle with PERIMETER.

    >>> near_golden(42) # 8 x 13 rectangle has perimeter 42
    8
    >>> near_golden(68) # 13 x 21 rectangle has perimeter 68
    13
    >>> result = near_golden(100) # return, don't print
    >>> result
    19

    """
    "*** YOUR CODE HERE ***"
    smallest_diff = 10
    result = "none"
    h = (perimeter / 2) - 1
    w = 1
    while h > 1:
        if (abs((h / w) - ((w / h) - 1)) < smallest_diff):
            result = h
            smallest_diff = (abs((h / w) - ((w / h) - 1)) < smallest_diff)
        h -= 1
        w += 1
    return result
        

