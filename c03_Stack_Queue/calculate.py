import time
from math import sqrt


def is_prime(x):
    for i in range(2, int(sqrt(x))):
        if x % i == 0:
            return False
    return True


if __name__ == '__main__':
    n = 707829217
    t1 = time.time()
    for i in range(int(sqrt(n)), n // 3):
        if n % i == 0:
            if is_prime(i):
                print(i)
                print(n / i)
                t2 = time.time()
                print(t2 - t1)
                break
