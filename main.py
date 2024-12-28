import time


# s = 'abc'
# s *= 2
# s = s.replace('c', 'x')
# print(s)

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b


def countdown(n):
    while n >= 0:
        mins, secs = divmod(n, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        n -= 1
    print('lift out!')


def galb():
    a, b, size = 0, 0, 15
    a = size // 2
    while a <= size:
        for b in range(1, b < size - a, 2):
            print('a')
        for b in range(1, b <= a, 1):
            print('A')
        for b in range(1, b <= size - 1, 1):
            print(' ')
        for b in range(1, b <= a-1, 1):
            print('A')
        print('')
        a += 2
    a = size
    while a >= 0:
        for b in range(a, b < size, 1):
            print(' ')
        for b in range(1, b <= (a * 2 - 1), 1):
            print('B')
        print()
        a -= 1


if __name__ == '__main__':
    galb()
