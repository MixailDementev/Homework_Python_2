# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

def fit_items_backpack(items, max_weight):
    backpack = []
    total_weight = 0
    
    for item, weight in items.items():
        if total_weight + weight <= max_weight:
            backpack.append(item)
            total_weight += weight
    
    return backpack

items = {
    "Тент": 2,
    "Коврик": 1.5,
    "Спальник": 1,
    "Палатка": 3,
    "Горелка": 0.5
}

max_weight = 6

result = fit_items_backpack(items, max_weight)
print(result)

