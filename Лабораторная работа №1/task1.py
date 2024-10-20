numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

missing_index = numbers.index(None)

sum_of_elements = sum([num for num in numbers if num is not None])

average = sum_of_elements / len(numbers)  # Количество элементов включает пропуск

# Заменяем пропущенный элемент средним арифметическим
numbers[missing_index] = average

# Выводим итоговый список

print("Измененный список:", numbers)
