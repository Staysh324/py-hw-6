# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. 
# не меньше заданного минимума и не больше заданного максимума)


def append_list(list, leng):
    numofelement = 1
    for i in range(leng):
        list_element = int(input(f"введите {numofelement} элемент строки: "))
        list.append(list_element)
        numofelement += 1
    return list

list = []
leng = int(input("введите размер массива: "))
append_list(list, leng)
min = int(input("введите минимум: "))
max = int(input("введите максимум: "))

for i in range (len(list)):
    if min <= list[i] <= max:
        print(f"значение {list[i]} с индексом {i} принадлежит списку")