from shapes import Circle, Triangle


def interactive_mode():
    print("Калькулятор площадей фигур")
    print("Доступные фигуры: circle, triangle")

    choice = input("Выберите фигуру: ").strip().lower()

    try:
        if choice == "circle":
            radius = float(input("Введите радиус: "))
            circle = Circle(radius)
            print(f"Площадь круга: {circle.area():.2f}")

        elif choice == "triangle":
            a = float(input("Сторона 1: "))
            b = float(input("Сторона 2: "))
            c = float(input("Сторона 3: "))

            triangle = Triangle(a, b, c)
            print(f"Площадь треугольника: {triangle.area():.2f}")
            print(f"Прямоугольный: {triangle.is_right_triangle()}")

        else:
            print("Неизвестная фигура")
    except ValueError:
        print("Ошибка: введите числовые значения")
    except Exception as e:
        print(f"Ошибка: {str(e)}")


if __name__ == "__main__":
    interactive_mode()