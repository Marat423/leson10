def get_matrix(n, m, value): # Создаем функцию
    matrix = [] # Создаем пустой список
    for i in range(n): # цикл
        matrix.append([]) # создаем/добавляем пустой список
        for j in range(m): # вложений цикл
            matrix[i].append(value) # во вложений список добавляем третье значение
    return matrix # возвращаем
   # print(matrix)


result1 = get_matrix(2, 2, 10) 
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)