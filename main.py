# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
"""
n = int(input("n = "))
m = int(input("m = "))

set_1 = {int(input(f"Введите {i + 1}е число множества n:")) for i in range(n)}
set_2 = {int(input(f"Введите {i + 1}е число множества m:")) for i in range(m)}

union_set = set_1.union(set_2)
union_list = list(union_set)
union_list.sort()

print(union_list, end=" ")
"""

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены
# только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод –
# на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля
# и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

"""
n = int(input("Количество кустов: "))
a = [int(input(f"Ягод на кусте {i+1}: ")) for i in range(n)]

max_count = 0
for i in range(n):
    if i < n - 1:
        right_count = a[i+1]
    else:
        right_count = a[0]
    count = a[i-1] + a[i] + right_count
    max_count = max(max_count, count)

print(f"Максимальное количество ягод: {max_count}")
"""