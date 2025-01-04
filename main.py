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


def question_chert_shirohi():
    #  Q1
    n = int(input('how meny number do you want: '))
    nummbers = []
    for i in range(n):
        num = int(input('>> '))
        nummbers.append(num)
    maximum = max(nummbers)
    if maximum % 5 == 0:
        for i in range(1000, 100, -1):
            if i % 6 == 0:
                print(i)
                break
    else:
        n2 = int(input('Enter a nummber to factorial: '))
        s = 1
        for i in range(n2, 1, -1):
            s *= i
        print(f'factorial {n2} is {s}')

    #  Q2
    sum = 0
    for i in range(2, 13):
        if i % 2 != 0:
            sum += i
    print(sum)

    #  Q3
    aa = ['red', 12, 'salam', 40, 'ww', 78, 12, 50, 45, 75, 'c++']
    mm = []
    for i in aa:
        if i.isdigit():
            mm.append(i)
    # mm = [i for i in aa if i.isdigit()]

    #  Q4
    my_list = ['red', 58, 'salam', 40, 'ww', 78, 'cpp']
    print(my_list[-1::-1])
    print(my_list[-1:-6:-2])
    my_list.insert(3, '20km')
    my_list.remove(78)
    print(my_list)


if __name__ == '__main__':
    pass























