"""Функции для вычисления площади и периметра круга."""
import math


def area(r):
    """Возвращает площадь круга радиуса r."""
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return math.pi * r ** 2


def perimeter(r):
    """Возвращает длину окружности радиуса r."""
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return 2 * math.pi * r
