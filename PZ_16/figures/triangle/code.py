a, b, c = 7, 2, 8


def triangle_perimeter(x=a, y=b, z=c):
    """Вычисляет периметр треугольника.
    Необходимы 3 стороны - 3 значения."""
    return x + y + z


def triangle_area(x=a, y=b, z=c):
    """Вычисляет площадь треугольника.
    Необходимы 3 стороны - 3 значения."""
    return (s * (s - x) * (s - y) * (s - z)) ** 0.5 if (s := (x + y + z) / 2) else 0
