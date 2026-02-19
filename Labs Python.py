import re

def is_valid_date(date_str: str) -> bool:
    """
    Проверяет, соответствует ли строка формату DD/MM/YYYY.
    """
    # Регулярное выражение для формата ДД/ММ/ГГГГ
    # \d{2} - две цифры, / - разделитель, \d{4} - четыре цифры
    pattern = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
    
    if re.match(pattern, date_str):
        return True
    return False

def get_validated_date(date_str: str) -> str:
    """
    Возвращает дату, если она корректна, иначе выбрасывает исключение.
    """
    if not is_valid_date(date_str):
        # Выбрасываем исключение о некорректном аргументе
        raise ValueError(f"Некорректный аргумент: '{date_str}' не является датой в формате DD/MM/YYYY")
    return date_str

if __name__ == "__main__":
    test_dates = ["12/05/2023", "32/01/2020", "01-01-2021", "05/13/2022", "abc"]
    
    for d in test_dates:
        print(f"Строка: {d} | Валидна: {is_valid_date(d)}")
        
    try:
        print(f"Результат функции: {get_validated_date('15/10/2024')}")
        print(get_validated_date("invalid-date"))
    except ValueError as e:
        print(e)