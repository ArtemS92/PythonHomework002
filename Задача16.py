# Задайте список из n чисел
# последовательности $(1+\frac 1 n)^n$
# и выведите на экран их сумму.


n = int(input('Введите число:'))
s = 0
for i in range(1, n + 1):
    # d = (1 + 1 / i) ** i
    print(f'{i}:{round((1 + 1 / i) ** i,2)}')
    s = s + (1 + 1 / i) ** i
# s = s + d
print(f'Сумма равна {round(s,2)}')
