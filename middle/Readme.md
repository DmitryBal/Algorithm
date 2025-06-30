# Middle level algorithm
## Содержание
- [TreeNumberSum](#TreeNumberSum.py)
- [SmallestDifference](#SmallestDifference.py)
- [KadanesAlgorithm](#KadanesAlgorithm.py)
- [HasSingleCycle](#HasSindleCycle.py)
- [Powerset](#Powerset.py)
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
## Из заданных чисел составить все возможные множества
