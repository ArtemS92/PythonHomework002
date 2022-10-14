# Реализуйте алгоритм перемешивания списка.


import random

n = int(input('Введите размер списка: '))
list1 = []
for i in range(n):
    list1.append(random.randint(-10, 10))
print(list1)

# random.shuffle(list1)

for i in range(len(list1) - 1, 0, -1):
    j = random.randint(0, i + 1)
    list1[i], list1[j] = list1[j], list1[i]
print(list1)
