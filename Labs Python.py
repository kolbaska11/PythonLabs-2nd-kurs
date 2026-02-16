def synonym_search():
    n = int(input("Введите количество пар синонимов: "))
    synonyms = {}
    
    for _ in range(n):
        word1, word2 = input().split()
        synonyms[word1] = word2
        synonyms[word2] = word1 # Синонимы работают в обе стороны
        
    query = input("Введите слово для поиска: ")
    print(synonyms.get(query, "Слово не найдено"))

if __name__ == "__main__":
    synonym_search()