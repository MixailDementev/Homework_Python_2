# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)

import time


class MyStr(str):
    """My class  comment"""

    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.start_time = time.strftime("%H:%M:%S", time.gmtime())
        instance.value = value
        return instance

    def __str__(self):
        return f"{self.value} Name author: {self.name}, time: {self.start_time}"


str_1 = MyStr(2, "Alex")

print(str_1)
print(MyStr.__doc__)
