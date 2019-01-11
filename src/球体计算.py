from math import pi


class Sphere:
    """编写一个程序，它以球体的半径（浮点数）作为输入，并且输出球体的直径、圆周长、表面积和体积。"""
    def __init__(self):  # 获取半径，并判断半径是否为数字
        while True:
            try:
                radius = input("请输入球体的半径：")
                self.radius = float(radius)
                break
            except ValueError:
                print("请输入数字！！！")

    def getdiameter(self):  # 计算直径
        diameter = self.radius * 2
        return diameter

    def getcircumference(self):  # 计算圆周长
        circumference = pi * self.radius * 2
        return circumference

    def getsuperficial_area(self):  # 计算表面积
        superficial_area = 4 * pi * self.radius**2
        return superficial_area

    def getvolume(self):  # 计算体积
        volume = (4 / 3) * pi * self.radius**3
        return volume


s = Sphere()
print("该球体的直径为{0:.2f}、圆周长为{1:.2f}、表面积为{2:.2f}、体积为{3:.2f}".format(
    s.getdiameter(), s.getcircumference(), s.getsuperficial_area(), s.getvolume()))
