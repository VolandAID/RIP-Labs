import time
from contextlib import contextmanager

class cm_timer_1:
    def __init__(self):
        self.begin_time = time.time()
    def __enter__(self):
        pass
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('time: ', time.time() - self.begin_time)


@contextmanager
def cm_timer_2():
    begin_time = time.time()
    yield 1
    print('time: ', time.time() - begin_time)


def main():
    with cm_timer_1():
        time.sleep(5.5)

    with cm_timer_2():
        time.sleep(2)


if __name__ == '__main__':
    main()