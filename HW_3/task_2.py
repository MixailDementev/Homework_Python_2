# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

def remove_duplicates(lst):
    return list(set(lst))

input_list = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(input_list)
print(result)

