# домашнее задание по теме "Функции"
# Объявляем функцию get_matrix с параметрами n, m и value
def get_matrix(n, m, value):
    # Создаем пустой список matrix
    matrix = []

    # Первый цикл для создания строк матрицы
    for _ in range(n):
        # Добавляем пустую строку в матрицу
        row = []
        # Внутренний цикл для заполнения строки значениями value
        for _ in range(m):
            row.append(value)
        # Добавляем заполненную строку в матрицу
        matrix.append(row)

    # Возвращаем созданную матрицу
    return matrix


# Примеры использования функции
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

# Выводим результаты на консоль
print(result1)
print(result2)
print(result3)

