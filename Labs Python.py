def election_results():
    import sys
    counts = {}
    
    print("Введите фамилии и количество голосов (Ctrl+D для завершения):")
    # Читаем строки до конца ввода
    for line in sys.stdin:
        if not line.strip(): break
        name, votes = line.split()
        counts[name] = counts.get(name, 0) + int(votes)
        
    # Выводим кандидатов в алфавитном порядке
    for name in sorted(counts.keys()):
        print(f"{name} {counts[name]}")

if __name__ == "__main__":
    election_results()