import math
import statistics
from typing import List

def circle_area(radius: float) -> float:
    """Функция для нахождения площади круга по заданному радиусу."""
    return math.pi * (radius ** 2)

def average_grade(grades: List[int]) -> int:
    """Функция для нахождения целого среднего балла по списку оценок."""
    return round(statistics.mean(grades))

def sber_securities(amount_of_money: float) -> int:
    """Функция для нахождения количества ценных бумаг Сбера, которые пользователь может купить по введенной сумме денег (на 15.04 стоимость 1 бумаги 317,20 р.)."""
    price_per_security = 317.20
    return int(amount_of_money // price_per_security)

# Пример использования внутри модуля
if __name__ == "__main__":
    print(circle_area(5))  # Площадь круга с радиусом 5
    print(average_grade([4, 5, 3, 4, 5]))  # Средний балл для списка оценок
    print(sber_securities(1000))  # Количество бумаг, которые можно купить на 1000 р.
