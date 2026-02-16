def find_most_frequent():
    import sys
    # Считываем весь текст и разбиваем на слова
    text = sys.stdin.read().split()
    counts = {}
    
    for word in text:
        counts[word] = counts.get(word, 0) + 1
        
    # Сортируем: сначала по частоте (в обратном порядке), 
    # затем по алфавиту (в прямом)
    # x[1] - количество, x[0] - само слово
    best_word = min(counts.keys(), key=lambda w: (-counts[w], w))
    
    print(best_word)

if __name__ == "__main__":
    find_most_frequent()