class Rectangle:
    def __init__(self, width, height=None):
        self.width = width
        self.height = height if height is not None else width

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def __add__(self, other):
        new_perimeter = self.perimeter() + other.perimeter()
        new_width = new_height = new_perimeter // 4
        return Rectangle(new_width, new_height)

    def __sub__(self, other):
        new_perimeter = abs(self.perimeter() - other.perimeter())
        new_width = new_height = new_perimeter // 4
        return Rectangle(new_width, new_height)

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __str__(self):
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

# Пример использования
rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)

print(f"Периметр rect1: {rect1.perimeter()}")
print(f"Площадь rect2: {rect2.area()}")
print(f"rect1 < rect2: {rect1 < rect2}")
print(f"rect1 == rect2: {rect1 == rect2}")
print(f"rect1 <= rect2: {rect1 <= rect2}")

rect3 = rect1 + rect2
print(f"Периметр rect3: {rect3.perimeter()}")

rect4 = rect1 - rect2
print(f"Ширина rect4: {rect4.width}")

# Вывод прямоугольников
print(rect1)
print(rect2)
print(rect3)
print(rect4)
