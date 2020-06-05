import time


def timethis(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        stop = time.time()
        print(f'{func.__module__}.{func.__name__}: {stop - start:0.4f}')
        return ret
    return wrapper


@timethis
def countdown(n):
    while n > 0:
        n -= 1


countdown(5_000_000)
