# Middle level algorithm
## Содержание
- [TreeNumberSum](#TreeNumberSum.py)
- [SmallestDifference](#SmallestDifference.py)
- [KadanesAlgorithm](#KadanesAlgorithm.py)
- [HasSingleCycle](#HasSindleCycle.py)
- [Powerset](#Powerset.py)
- [SearchInSortedMatrix](#SearchInSortedMatrix.py)
- [BalancedBrackets](#BalancedBrackets.py)
- [LongestPalindromicSubstring](#LongestPalindromicSubstring.py)
## TreeNumberSum 
### Найти все группы из трех чисел в массиве, сумма которых равна заданной сумме 
#### def threeNumberSum(array, targetSum)
- Принимает на вход: массив и число
- Возвращает: массивы из трех чисел

## SmallestDifference
### Из двух массивов найти два числа с минимальной разницей
#### def smallestDifference(arr1, arr2)
- Принимает на вход: два массива
- Возвращает: массив из двух чисел

## KadanesAlgorithm
### Найти максимальную сумму непрерывного подмассива в заданном массиве
#### def kadanesAlgorithm(array)
- Принимает на вход: массив
- Возвращает: максимальную сумму подмассива 

## HasSingleCycle
### Образуют ли элементы массива кольцо. (нужно сдвигаться на элемент равный значению массива)
#### def hasSingleCycle(array)
- Принимает на вход: массив
- Возвращает: True/False
#### def getNextInd(current_index, array)
- Принимает на вход: текущий индекс, массив
- Возвращает: индекс следующего элемента по возможному кольцу

## Powerset
### Из заданных чисел составить все возможные множества
#### def powerset_iteration(array) - итерационное решение
- Принимает на вход: массив
- Возвращает: Массив из всех возможных множеств
#### def powerset_recursion(array) - рекурсивное решение
- Принимает на вход: массив
- Возвращает: Массив из всех возможных множеств
## SearchInSortedMatrix
### Поиск в отсортированной матрице
#### deft searchInSortedMatrix(matrix, target)
- Принимает на вход: матрицу и число
- Возвращает: массив с индексами числа в матрице
## BalancedBrackets
### Проверка на корректность закрытия скобок
#### def balancedBrackets(string)
- Принимает на вход: строку
- Возвращает: True/False
## LongestPalindromicSubstring
### Поиск максимального полиндрома в строке
#### def longestPalindromicSubstring(string)
- Принимает на вход: строку
- Возвращает: максимальный полиндрома
#### def getLongestPolindrome(string, left_index, right_index)
- Принимает на вход: строку и два индекса
- Возвращает: массив индексов для найденого полиндрома 
