def find_greatest_common_divisor(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    res = a + b
    return res

