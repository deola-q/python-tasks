# Для набора прямоугольников, стороны которых параллельны OX и OY, заданных координатами 2-х диагональных вершин,
# найти прямоугольник, внутри которого расположено максимальное кол-во других прямоугольников
# (граница вложенного прямоугольника может проходить по границе внешнего прямоугольника). В случае существования
# нескольких подходящих прямоугольников – выбрать максимальной площади (если и таких будет несколько – то произвольный).
# 9. Задача 6, только применительно к набору окружностей (кругов).
import math


class Circle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = min(x1, x2)
        self.y1 = min(y1, y2)
        self.x2 = max(x1, x2)
        self.y2 = max(y1, y2)
        self.radius = self.calculate_radius()

    def calculate_radius(self):
        return math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) / 2


def is_inside(circle1, circle2):
    distance = math.sqrt((circle1.x1 - circle2.x1) ** 2 + (circle1.y1 - circle2.y1) ** 2)
    return distance + circle2.radius <= circle1.radius


def find_maximum_circle(circles):
    max_count = 0
    max_circle = None
    for circle in circles:
        count = sum(is_inside(circle, other_circle) for other_circle in circles)
        if count > max_count or (count == max_count and circle.radius > max_circle.radius):
            max_count = count
            max_circle = circle
    return max_circle


def test_function():
    with open('input3.txt', 'r') as f:
        m = []
        for line in f:
            vertices = [int(i) for i in line.strip().split()]
            m.append(vertices)
        print(m)
        circles = [Circle(m[i][0], m[i][1], m[i][2], m[i][3]) for i in range(0, len(m))]

    max_circle = find_maximum_circle(circles)
    answer = [max_circle.x1, max_circle.y1, max_circle.x2, max_circle.y2]
    with open('output3.txt', 'w') as f:
        f.write(" ".join(map(str, answer)))


test_function()
