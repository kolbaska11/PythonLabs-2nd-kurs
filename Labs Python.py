#Лабораторная 1, В - 2
import math

# Функция 1
def count_coprime(n):
    count = 0
    for i in range(1, n + 1):
        if math.gcd(n, i) == 1:
            count += 1
    return count

#Функция 2
def sum_digits_div_3(n):
    return sum(int(d) for d in str(abs(n)) if int(d) % 3 == 0)