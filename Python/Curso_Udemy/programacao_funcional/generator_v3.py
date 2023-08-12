def sequence():
    x = 0
    while True:
        x += 1
        yield x



if __name__ == '__main__':
    seq = sequence()

    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    