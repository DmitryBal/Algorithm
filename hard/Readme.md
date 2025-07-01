# Hard level algorithm
## Содержание
- [FourNumberSum](#FourNumberSum.py)
- [SubarraySort](#SubarraySort.py)
- [LargestRange](#LargestRange.py)

## FourNumberSum
### Найти все группы из четырех чисел в массиве, сумма которых равна заданной сумме
#### def fourNumberSum(array, target_sum)
- Принимает на вход: массив и число
- Возвращает: массивы из четырех чисел

## SubarraySort
### Определить границы неотсортированной части массива
#### def isOutOfOrder(i, num, array)
- Принимает на вход: индекс, число и массив
- Возвращает True/False (является определенный элемент массива не отсоритрованным)
#### def subarraySort(array)
- Принимает на вход: массив
- Возвращает: массив из двух индексов (границы неотсортированной части массива)

## LargestRange
### Максимальное количество чисел идущих подряд
#### def largestRange(array)
Принимает на вход: массив
Возвращает: массив из 2 чисел (Min/Max чисел из подряда)
