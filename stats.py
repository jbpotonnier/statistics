from math import sqrt, ceil

def mean(v):
     """ 
     >>> mean([1, 3, 4.5, 5]) == (1 + 3 + 4.5 + 5) / 4.0
     True
     """
     return sum(e for e in v) / float(len(v))


def variance(m, v):
    """
    >>> v = [1, 3, 4.5, 6.5]
    >>> m = mean(v)
    >>> (1.0 / 4) * ((1 - m)**2 + (3 - m)**2 + (4.5 - m)**2 + (6.5 - m)**2)
    4.0625
    >>> variance(m, v)
    4.0625
    """
    return (1.0 / len(v)) * sum((e - m)**2 for e in v)


def mean_var(v):
    """
    >>> mean_var([1, 2, 3, 4])
    (2.5, 1.25)
    >>> v = [1, 3, 4.5, 6.5]
    >>> m = mean(v)
    >>> mean_var(v) == (m, variance(m, v))
    True
    """
    s = 0
    ss = 0
    for e in v:
        s += e
        ss += e**2
    m = s / float(len(v))
    mss = ss / float(len(v))
    return (m, mss - m**2)


def median(v, already_sorted=False):
    """
    >>> median([12, 5, 6, 89, 5, 2390, 1])
    6
    >>> median([12, 5, 6, 89, 5, 1])
    5.5
    """
    length = len(v)
    sorted_v = v if already_sorted else sorted(v)
    return sorted_v[length / 2] if length % 2 != 0 else mean([sorted_v[length/2 - 1], sorted_v[length/2]])


def quartile_1(v, already_sorted=False):
    """
    >>> v = [20, 11, 19, 24, 28, 1, 34, 37, 15, 47, 50, 57]
    >>> quartile_1(v)
    15
    """
    index = int(ceil(len(v) / 4)) - 1
    sorted_v = v if already_sorted else sorted(v)
    return sorted_v[index]


def quartile_3(v, already_sorted=False):
    """
    >>> v = [20, 11, 19, 24, 28, 1, 34, 37, 15, 47, 50, 57]
    >>> quartile_3(v)
    37
    """
    index = (int(ceil(len(v) / 4)) * 3) - 1
    sorted_v = v if already_sorted else sorted(v)
    return sorted_v[index]


def quartiles(v):
    """
    >>> v = [20, 11, 19, 24, 28, 1, 34, 37, 15, 47, 50, 57]
    >>> quartiles(v)
    (15, 26.0, 37)
    """
    sorted_v = sorted(v)
    return (quartile_1(sorted_v, True), median(sorted_v, True), quartile_3(sorted_v, True))
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
