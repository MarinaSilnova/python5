#Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
import random
random_list = [random.randint(1,11) for _ in range(15)]
print(f'изначальный список : {random_list}')
count = {el for el in random_list if random_list.count(el)>1}
print (f'повторяющиеся элементы : {count}')
print(f'количество повторяющихся элементов : {len(count)}')
finish_list = []
# for i in random_list:
#     if i not in finish_list:
#         finish_list.append(i)
finish_list = list(set(random_list))
print(f'список уникальных элементов {finish_list} ')

