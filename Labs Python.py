import string

def solve_task_2(filename):
    count = 0
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                # Очищаем строку от знаков препинания и делим на слова
                words = line.split()
                for word in words:
                    # Убираем лишние знаки вокруг слова
                    clean_word = word.strip(string.punctuation).lower()
                    
                    # Проверяем условие (слово должно быть длиннее 1 символа)
                    if len(clean_word) > 0:
                        if clean_word[0] == clean_word[-1]:
                            count += 1
        return count
    except FileNotFoundError:
        return "Файл не найден"

print(f"Количество слов: {solve_task_2('text.txt')}")