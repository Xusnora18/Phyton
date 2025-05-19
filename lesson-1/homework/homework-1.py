# Домашнее задание — 4 задачи с функциями

# Задание 1: Периметр и площадь квадрата
def square_info(side):
    perimeter = 4 * side
    area = side * side
    print("Периметр:", perimeter)
    print("Площадь:", area)

# Задание 2: Длина окружности по диаметру
def circle_length(diameter):
    length = 3.14 * diameter
    print("Длина окружности:", length)

# Задание 3: Среднее значение двух чисел
def mean(a, b):
    result = (a + b) / 2
    print("Среднее значение:", result)

# Задание 4: Сумма, произведение и квадраты
def number_operations(a, b):
    print("Сумма:", a + b)
    print("Произведение:", a * b)
    print("Квадрат a:", a ** 2)
    print("Квадрат b:", b ** 2)

# Примеры вызова (можно заменить input() на свои значения)
if __name__ == "__main__":
    # Задание 1
    side = float(input("Введите сторону квадрата: "))
    square_info(side)

    # Задание 2
    d = float(input("Введите диаметр круга: "))
    circle_length(d)

    # Задание 3
    a = float(input("Введите число a: "))
    b = float(input("Введите число b: "))
    mean(a, b)

    # Задание 4
    number_operations(a, b)
