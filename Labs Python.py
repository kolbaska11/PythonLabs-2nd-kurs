#Лабораторная 1, В - 2
import math

# Функция 1: Количество чисел, взаимно простых с N [cite: 16]
def count_coprime(n):
    count = 0
    for i in range(1, n + 1):
        if math.gcd(n, i) == 1:
            count += 1
    return count

# Функция 2: Сумма цифр числа, делящихся на 3 [cite: 17]
def sum_digits_div_3(n):
    return sum(int(d) for d in str(abs(n)) if int(d) % 3 == 0)

# Функция 3: Делитель, взаимно простой с суммой цифр числа [cite: 18, 19]
def divisor_coprime_with_sum(n):
    digits_sum = sum(int(d) for d in str(abs(n)))
    for i in range(2, n + 1):
        if n % i == 0 and math.gcd(i, digits_sum) == 1:
            return i
    return None