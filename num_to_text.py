numbers = {0: 'teg', 1: 'neg', 2: 'hoyor', 
3: 'gurav', 4: 'duruv', 5: 'tav', 6: 'zurgaa',
7: 'doloo', 8: 'naim', 9: 'yus', 10: 'arav',
20: 'hori', 30: 'guch', 40: 'duch', 50: 'tavi',
60: 'jar', 70: 'dal', 80: 'nay', 90: 'yer',
100: 'zuu'}

numbers2 = {0: '', 1: 'neg', 2: 'hoyor', 
3: 'gurvan', 4: 'durvun', 5: 'tavan', 6: 'zurgaan',
7: 'doloon', 8: 'naiman', 9: 'yusun', 10: 'arvan ',
20: 'horin ', 30: 'guchin ', 40: 'duchin ', 50: 'tavin ',
60: 'jaran ', 70: 'dalan ', 80: 'nayan ', 90: 'yeren '}

n = int(input("Enter value: "))
if n < 10:
    text = numbers[n]
elif n < 100:
    if n % 10 == 0:
        text = numbers[n]
    else:
        m = n // 10 * 10
        r = n % 10
        text = numbers2[m] + ' ' + numbers[r]
else: 
    if n % 100 == 0:
        k = n // 100
        text = numbers2[k] + ' zuu'
    else:
        if n % 10 == 0:
            k = n // 100
            r = n % 100
            text = numbers2[k] + ' zuun ' + numbers[r]
        else:
            k = n // 100
            r = (n % 100) // 10 * 10
            d = n % 10
            text = numbers2[k] + ' zuun ' + numbers2[r] + numbers[d]
print(text)