import my_module


def main():
    # Проверка функции нахождения площади круга
    radius = 5.0
    print(f"Площадь круга с радиусом {radius}: {my_module.circle_area(radius)}")

    # Проверка функции нахождения целого среднего балла
    grades = [4, 5, 3, 4, 5]
    print(f"Целый средний балл для оценок {grades}: {my_module.average_grade(grades)}")

    # Проверка функции нахождения количества ценных бумаг Сбера
    amount_of_money = 1000.0
    print(
        f"Количество ценных бумаг Сбера, которые можно купить на {amount_of_money} р: {my_module.sber_securities(amount_of_money)}")


if __name__ == "__main__":
    main()
