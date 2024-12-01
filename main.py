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

zarb()