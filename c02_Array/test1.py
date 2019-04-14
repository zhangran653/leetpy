if __name__ == '__main__':
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('{} * {} = {}  '.format(j, i, j * i), end='')
        print()