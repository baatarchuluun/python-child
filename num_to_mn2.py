"""Given an int32 number, print it in English."""
def int_to_mn(num, ind):
    d = { 0 : 'тэг', 1 : 'нэг', 2 : 'хоёр', 3 : 'гурав', 4 : 'дөрөв', 5 : 'тав',
          6 : 'зургаа', 7 : 'долоо', 8 : 'найм', 9 : 'ес', 10 : 'арав',
          20 : 'хорь', 30 : 'гуч', 40 : 'дөч', 50 : 'тавь', 60 : 'жар',
          70 : 'дал', 80 : 'ная', 90 : 'ер' }
    d2 = { 1 : 'нэг', 2 : 'хоёр', 3 : 'гурван', 4 : 'дөрвөн', 5 : 'таван',
          6 : 'зургаан', 7 : 'долоон', 8 : 'найман', 9 : 'есөн', 10 : 'арван',
          20 : 'хорин', 30 : 'гучин', 40 : 'дөчин', 50 : 'тавин', 60 : 'жаран',
          70 : 'далан', 80 : 'наян', 90 : 'ерэн' }

    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000

    assert(0 <= num)

    if (num < 10):
        if ind == 1: 
            return d2[num]
        return d[num]

    if (num < 100):
        if num % 10 == 0: 
            if ind == 1:
                return d2[num]
            return d[num]
        else: 
            if ind == 1: return d2[num // 10 * 10] + ' ' + d2[num % 10]
            else: return d2[num // 10 * 10] + ' ' + d[num % 10]

    if (num < k):
        if num % 100 == 0: return d[num // 100] + ' зуу'
        else: return d2[num // 100] + ' зуун ' + int_to_mn(num % 100, 1)

    if (num < m):
        if num % k == 0: return int_to_mn(num // k, 1) + ' мянга'
        else: return int_to_mn(num // k, 1) + ' мянга ' + int_to_mn(num % k, 1)

    if (num < b):
        if (num % m) == 0: return int_to_mn(num // m, 1) + ' сая'
        else: return int_to_mn(num // m, 1) + ' сая ' + int_to_mn(num % m, 1)

    if (num < t):
        if (num % b) == 0: return int_to_mn(num // b, 1) + ' тэрбум'
        else: return int_to_mn(num // b, 1) + ' тэрбум ' + int_to_mn(num % b, 1)

    if (num % t == 0): return int_to_mn(num // t, 1) + ' триллион'
    else: return int_to_mn(num // t, 1) + ' триллион ' + int_to_mn(num % t, 1)

    raise AssertionError('num is too large: %s' % str(num))

n = int(input("Enter value: "))
print(int_to_mn(n, 0))