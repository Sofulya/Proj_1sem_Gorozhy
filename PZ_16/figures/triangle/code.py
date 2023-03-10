a, b, c = 7, 2, 8


def triangle_perimeter(x=a, y=b, z=c):
    return x + y + z


def triangle_area(x=a, y=b, z=c):
    return (p * (p - x) * (p - y) * (p - z)) ** 0.5 if (p := (x + y + z) / 2) else 0
