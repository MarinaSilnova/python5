#Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию.
import random
length = 15
numbers = [random.randint(1,10) for _ in range(length)]
print(numbers)
result = list(filter(lambda x: x > 5, numbers))
print(result)