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

# #Функция 4 задание 2
# import os

# def task_2():
#     """Проверка упорядоченности строчной латиницы"""
#     s = input("Введите строку: ")
#     lowers = [c for c in s if 'a' <= c <= 'z']
#     if lowers == sorted(lowers):
#         print("Символы упорядочены.")
#     else:
#         print("Символы не упорядочены.")

# #Функция 5 задание 10
# def task_10():
#     """Подсчет количества букв 'А'"""
#     s = input("Введите строку: ")
#     # Считаем и латинские 'A', и русские 'А' (регистр не важен)
#     count = s.upper().count('A') + s.upper().count('А')
#     print(f"Количество букв А: {count}")

# #Функция 6 задание 17
# def task_17():
#     """Имя файла без расширения"""
#     path = input("Введите путь к файлу: ")
#     name = os.path.basename(path)
#     print(f"Имя файла: {os.path.splitext(name)[0]}")

# #Функция 7, она же main
# def main():
#     print("1 - Проверка латиницы\n2 - Подсчет 'А'\n3 - Имя файла")
#     choice = input("Выберите задачу: ")
#     if choice == '1': task_2()
#     elif choice == '2': task_10()
#     elif choice == '3': task_17()

# if __name__ == "__main__":
#     main()

def list_task_2(arr):
    """Индекс минимального элемента"""
    return arr.index(min(arr))

def list_task_14_38(arr, a, b):
    """Количество элементов в интервале a..b"""
    return len([x for x in arr if a <= x <= b])

def list_task_26(arr):
    """Количество элементов между первым и последним минимальным"""
    if not arr: return 0
    min_val = min(arr)
    first = arr.index(min_val)
    last = len(arr) - 1 - arr[::-1].index(min_val)
    return max(0, last - first - 1)