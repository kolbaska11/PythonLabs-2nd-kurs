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
            raise InvalidDataError("Идентификатор не может быть пустым")
        self.id = identifier  # Идентификатор в виде строки 
        self.x = x            # Поля для хранения состояния
        self.y = y

    def move(self, dx: float, dy: float):
        """Метод перемещения объекта на плоскости [cite: 12]"""
        self.x += dx
        self.y += dy
        print(f"Объект {self.id} перемещен в точку ({self.x}, {self.y})")

    def get_area(self) -> float:
        return 0.0