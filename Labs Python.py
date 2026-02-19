def solve_task_1(filename):
    with open(filename, 'r') as f:
        # Читаем N и K из первой строки
        line = f.readline().split()
        if not line: return
        n, k = map(int, line)
        
        # Читаем все числа в список
        data = [int(line) for line in f if line.strip()]

    # Инициализируем переменные для поиска минимумов
    # min_1: минимальное число на расстоянии >= 2K от текущего
    # min_2: минимальное произведение двух чисел на расстоянии >= K
    min_1 = float('inf')
    min_2 = float('inf')
    min_3 = float('inf')

    # Идем по списку, считая текущий элемент третьим (index_3)
    for index_3 in range(2 * k, n):
        # Элемент, который может быть первым
        index_1 = index_3 - 2 * k
        if data[index_1] < min_1:
            min_1 = data[index_1]
            
        # Элемент, который может быть вторым
        index_2 = index_3 - k
        if min_1 * data[index_2] < min_2:
            min_2 = min_1 * data[index_2]
            
        # Текущий элемент как третий
        if min_2 * data[index_3] < min_3:
            min_3 = min_2 * data[index_3]

    # Результат — остаток от деления на 10^6 + 1
    return int(min_3 % (10**6 + 1))

print(solve_task_1("27-167a.txt"), solve_task_1("27-167b.txt"))