def test1(a, b, c):
    if a > b:
        print('Great! A equals to ' + str(a) + ' and is bigger then B, that equals ' + str(b))
    elif a == b:
        print('Great! A = ' + str(a) + ' equals to B = ' + str(b))

    while a < b:
        a += c

        return test1(a, b, c)

test1(2, 51, 6)
