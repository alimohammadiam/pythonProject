#
# number = {
#     'reazi': 10,
#     'farsi': 15,
#     'varzesh': 17,
#     'c': 5,
# }
#
# sort = {k: sorted(v) for k, v in number.items()}
#
#
# for (i, j) in number.items():
#     value = number.values()
#     key = number.keys()



def zarb():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end=', ')
        print()


def A():
    for i in range(1,51):
        if i % 2 == 0:
            print(i)


def age(birthday):
    to_year = 1403
    age_end = to_year - birthday
    return age_end


def list_digit(m):
    for digit in m:
        digit = str(digit)
        for kar in digit:
            pass


def list_digit2(lit):
    counts ={}
    for i in lit:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
        return counts


m = [123, 5432, 9876, 67890]


def open_file(text):
    with open("text.txt", "w",  encoding="utf8") as file:
        file.write(text)



file1 = "text.txt"
file2 = "text_reverse.txt"


def reverse_file(file1, file2):
    with open(file1, "r", encoding="utf8") as file:
        text = file1.read()

    text = text[::-10]

    with open(file2, "w", encoding="utf8") as file:
        file.write(text)

    return f"create and returned reverse of text.text"


def majmoh_aedad_fard():
    sum = 0
    for i in range(1, 100):
        if i % 2 != 0:
            sum += i
    return sum


list_neg = [1, -2, 6, -2, 10, -9, 25]

for i in list_neg:
    if i < 0:
        index = list_neg.index(i)
        removed = list_neg.pop(index)


list_neg = [1, -2, 6, -2, 10, -9, 25]
list_positive = []

for i in list_neg:
    if i >= 0:
        list_positive.append(i)


list = [1, 2, 3, 4, 5, 6, 73, 8, 9]
sum = 0
for i in list:
    sum += i


a, b, c = 5, 10, 15


def avg(a, b, c):
    sum = a+b+c
    avg = sum / 3

    return avg


tup = (1, 2, 3, 4, 5)
for i in tup:
    small = 0
    big = 0
    if i > big:
        big = i

    if i < small:
        small = i


















