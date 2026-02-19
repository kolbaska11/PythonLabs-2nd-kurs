import math

class ShapeError(Exception):
    """Базовый класс для исключений в лабораторной работе """
    pass

class InvalidDataError(ShapeError):
    """Ошибка при некорректных входных данных"""
    pass

class BaseShape:
    def __init__(self, identifier: str, x: float = 0, y: float = 0):
        if not identifier:
            raise InvalidDataError("Идентификатор не может быть пустым [cite: 9]")
        self.id = identifier  # Идентификатор в виде строки [cite: 9]
        self.x = x            # Поля для хранения состояния [cite: 9]
        self.y = y

    def move(self, dx: float, dy: float):
        """Метод перемещения объекта на плоскости [cite: 12]"""
        self.x += dx
        self.y += dy
        print(f"Объект {self.id} перемещен в точку ({self.x}, {self.y})")

    def get_area(self) -> float:
        return 0.0

class Triangle(BaseShape):
    def __init__(self, identifier: str, a: float, b: float, c: float, x=0, y=0):
        super().__init__(identifier, x, y)
        # Проверка существования треугольника (обработка исключений )
        if a + b <= c or a + c <= b or b + c <= a:
            raise InvalidDataError(f"Треугольник {identifier} с такими сторонами не существует")
        self.a, self.b, self.c = a, b, c

    def get_area(self) -> float:
        """Расчет площади по формуле Герона"""
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

class Quad(BaseShape):
    def __init__(self, identifier: str, side: float, x=0, y=0):
        super().__init__(identifier, x, y)
        if side <= 0:
            raise InvalidDataError(f"Сторона квадрата {identifier} должна быть положительной")
        self.side = side

    def get_area(self) -> float:
        return self.side ** 2