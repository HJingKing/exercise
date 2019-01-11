from math import pi


class Sphere:
    """编写一个程序，它以球体的半径（浮点数）作为输入，并且输出球体的直径、圆周长、表面积和体积。"""
    def __init__(self, radius):
        self.radius = radius

    def getdiameter(self):
        diameter = self.radius * 2
        return diameter

    def getcircumference(self):
        circumference = pi * self.radius * 2
        return circumference

    def getsuperficial_area(self):
        superficial_area = 4 * pi * self.radius**2
        return superficial_area

    def getvolume(self):
        volume = (4 / 3) * pi * self.radius**3
        return volume


r = float(input("请输入球体的半径："))
s = Sphere(r)
print("该球体的直径为{0:.2f}、圆周长为{1:.2f}、表面积为{2:.2f}、体积为{3:.2f}".format(s.getdiameter(), s.getcircumference(),
                                                             s.getsuperficial_area(), s.getvolume()))
