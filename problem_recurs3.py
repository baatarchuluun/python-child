# өгөгдсөн тооны цифрүүдийн нийлбэр
def sum_digit(n):
    if n // 10 == 0:
        return n
    else:
        return n % 10 + sum_digit(n // 10)

def count_digit(n):
    if n // 10 == 0:
        return 1
    else:
        return 1 + count_digit(n // 10)

print(count_digit(325))