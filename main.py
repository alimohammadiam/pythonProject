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


if __name__ == '__main__':
    countdown(10)