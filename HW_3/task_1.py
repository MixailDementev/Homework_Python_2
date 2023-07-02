# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
# 1) Какие вещи взяли все три друга
# 2) Какие вещи уникальны, есть только у одного друга и имя этого друга
# 3) Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

friends_items = {
    "Друг 1": ("палатка", "спальник", "фонарик"),
    "Друг 2": ("палатка", "продукты", "карта"),
    "Друг 3": ("палатка", "спички", "фонарик"),
}

common_items = set.intersection(*[set(items) for items in friends_items.values()])
print("Вещи, которые взяли все три друга:", common_items)

unique_items = set()
unique_friends = {}

for friend, items in friends_items.items():
    for item in items:
        if item not in common_items:
            unique_items.add(item)
            unique_friends[item] = friend

print("Уникальные вещи и имена друзей, у которых они есть:")
for item, friend in unique_friends.items():
    print(f"{item}: {friend}")

missing_items = set()
missing_friend = {}

for item in common_items:
    present_friends = [
        friend for friend, items in friends_items.items() if item in items
    ]
    if len(present_friends) < len(friends_items) - 1:
        missing_items.add(item)
        missing_friend[item] = [
            friend for friend in friends_items.keys() if friend not in present_friends
        ][0]

print("Вещи, которые есть у всех, кроме одного друга, и имя этого друга:")
for item, friend in missing_friend.items():
    print(f"{item}: {friend}")
