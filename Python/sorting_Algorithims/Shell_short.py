# Python program for implementation of Shell Sort

def shellSort(arr):
    # Start with a big gap, then reduce the gap

    n = len (arr)
    gap = n / 2

    # Do a gapped insertion sort for this gap size.
    # The first gap elemtns a[]