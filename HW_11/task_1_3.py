# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения


class Rectangle:
    """Создание прямоугольника, вычисление периметров, сравнение по площади"""

    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width else length

    def get_perimetr(self):
        return 2 * (self.length + self.width)

    def get_area(self):
        return self.length * self.width

    def __add__(self, other):
        return Rectangle(self.length + other.length, self.width + other.width)

    def __sub__(self, other):
        return Rectangle(abs(self.length - other.length), abs(self.width - other.width))

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        return self.get_area() != other.get_area()

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() <= other.get_area()

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __le__(self, other):
        return self.get_area() >= other.get_area()

    def __str__(self):
        return f"Прямоугольник со сторонами: {self.length}, {self.width} и периметром {self.get_perimetr()}"


if __name__ == "__main__":
    a = Rectangle(6, 2)
    b = Rectangle(7, 4)
    c = a + b
    d = a - b
    print(f"Периметр a: {a.get_perimetr()}, Периметр b: {b.get_perimetr()}")
    print(c)
    print(d)
    print(a == b)
    print(a != b)
    print(a > b)
    print(a <= b)
    print(a < b)
    print(a >= b)
    print(Rectangle.__doc__)
