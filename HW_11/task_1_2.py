# Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов
# list-архивы также являются свойствами экземпляра

# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста и для пользователя.


class Archive:
    """Архив, который хранит пару свойств.
    При нового экземпляра класса, старые данные из ранее cозданных экземпляров сохраняются в пару списковархивов  list-архивы также являются свойствами экземпляра
    добавить repr"""

    _instance = None

    def __init__(self, number, archive_string):
        self.number = number
        self.archive_string = archive_string

    def __new__(cls, *args):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_list = []
        else:
            cls._instance.archive_list.append(
                (cls._instance.number, cls._instance.archive_string)
            )
        return cls._instance

    def __str__(self):
        return f"Number: {self.number}, Name data: {self.archive_string}, Archive: {self.archive_list}"

    def __repr__(self):
        return f'Archive: ({self.number}, "{self.archive_string}")'


u_1 = Archive(1, "One book")
# print(f"{u_1.number = },{u_1.archive_string = }, {u_1.archive_list = }")
print(u_1)
u_2 = Archive(2, "Two book")
print(u_2)
u_3 = Archive(3, "Three book")
print(u_3)
print(repr(u_3))
u_4 = repr(u_3)
print(u_4)
print(Archive.__doc__)
