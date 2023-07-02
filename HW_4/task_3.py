# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


def hashtable_dicts(**kwargs):
    pets = dict()
    for k, v in kwargs.items():
        if isinstance(v, (list, dict, set, bytearray)):
            v = str(v)
        pets[v] = k
    return pets


print(
    hashtable_dicts(
        dog="Jackill",
        cat={"Leopold": 2, "Murka": 3},
        turtle=["Bill", "Jack", "Anatoliy"],
        hamster={"Edward", "Homa"},
    )
)
