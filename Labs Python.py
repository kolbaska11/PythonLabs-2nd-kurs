# #Лабораторная 1, В - 2
# import math

# # Функция 1
# def count_coprime(n):
#     count = 0
#     for i in range(1, n + 1):
#         if math.gcd(n, i) == 1:
#             count += 1
#     return count

# #Функция 2
# def sum_digits_div_3(n):
#     return sum(int(d) for d in str(abs(n)) if int(d) % 3 == 0)

# #Функция 3
# def divisor_coprime_with_sum(n):
#     digits_sum = sum(int(d) for d in str(abs(n)))
#     for i in range(2, n + 1):
#         if n % i == 0 and math.gcd(i, digits_sum) == 1:
#             return i
#     return None

#Функция 4
import os

def task_2():
    """Проверка упорядоченности строчной латиницы"""
    s = input("Введите строку: ")
    lowers = [c for c in s if 'a' <= c <= 'z']
    if lowers == sorted(lowers):
        print("Символы упорядочены.")
    else:
        print("Символы не упорядочены.")

