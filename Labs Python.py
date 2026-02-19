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
        """Метод перемещения объекта на плоскости """
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
    
def compare(t1: BaseShape, t2: BaseShape):
    """Сравнение объектов по площади """
    area1 = t1.get_area()
    area2 = t2.get_area()
    if area1 > area2:
        return f"Площадь {t1.id} ({area1:.2f}) больше {t2.id} ({area2:.2f})"
    elif area1 < area2:
        return f"Площадь {t1.id} ({area1:.2f}) меньше {t2.id} ({area2:.2f})"
    return "Площади равны"

if __name__ == "__main__":
    try:
        # Создание объектов 
        tri = Triangle("Tri_Alpha", 3, 4, 5, x=10, y=10)
        sq = Quad("Quad_Beta", 4, x=0, y=0)

        # Демонстрация методов 
        print(f"Объект: {tri.id}, Площадь: {tri.get_area()}")
        print(f"Объект: {sq.id}, Площадь: {sq.get_area()}")
        
        tri.move(5, -2)       # Метод move 
        print(compare(tri, sq)) # Метод compare 

        # Пример вызова исключения 
        bad_tri = Triangle("Error_Tri", 1, 1, 10) 

    except InvalidDataError as e:
        print(f"Поймано исключение: {e} ")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")