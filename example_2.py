class Element:
    def __add__(self, other):
        return None

    def __str__(self):
        return self.__class__.__name__

class Water(Element):
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Mud()
        return None

class Air(Element):
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        return None

class Fire(Element):
    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Earth):
            return Lava()
        return None

class Earth(Element):
    def __add__(self, other):
        if isinstance(other, Water):
            return Mud()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        return None

class Storm(Element):
    def __str__(self):
        return "Шторм"

class Steam(Element):
    def __str__(self):
        return "Пар"

class Mud(Element):
    def __str__(self):
        return "Грязь"

class Lightning(Element):
    def __str__(self):
        return "Молния"

class Dust(Element):
    def __str__(self):
        return "Пыль"

class Lava(Element):
    def __str__(self):
        return "Лава"

# Дополнительный элемент
class Ice(Element):
    def __add__(self, other):
        if isinstance(other, Fire):
            return Water()
        elif isinstance(other, Earth):
            return Frost()
        return None

class Frost(Element):
    def __str__(self):
        return "Иней"

# Пример использования
water = Water()
air = Air()
fire = Fire()
earth = Earth()
ice = Ice()

# Тестирование комбинаций
print(f"Вода + Воздух = {water + air}")
print(f"Вода + Огонь = {water + fire}")
print(f"Вода + Земля = {water + earth}")
print(f"Воздух + Огонь = {air + fire}")
print(f"Воздух + Земля = {air + earth}")
print(f"Огонь + Земля = {fire + earth}")
print(f"Лёд + Огонь = {ice + fire}")
print(f"Лёд + Земля = {ice + earth}")
