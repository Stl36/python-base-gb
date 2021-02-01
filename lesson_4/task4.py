"""
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""
from random import randint

main_list = []
for item in range(5, randint(7, 50)):
    number = randint(0, 100)
    main_list.append(number)
print(f"Сгенерированный список {main_list}\n"
      f"Отфильтрованный список {[item for item in main_list if main_list.count(item) == 1]}")