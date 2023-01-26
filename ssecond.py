#Дан список случайных чисел. Создайте список, в который попадают числа, описывающие случайную возрастающую последовательность. Порядок элементов менять нельзя.
import random
length = 15
numbers = list(random.randint(1,111) for _ in range(length))
print(numbers)
max = numbers[2]
result = [max]
for el in filter(lambda x: x>max, numbers[2:]):
    result.append(el)
    max=el
print(result)