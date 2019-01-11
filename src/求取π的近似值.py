class Pi(object):
    """德国数学家Gottfried Leibniz 为求取π的近似值开发了如下方法：π/4 = 1 - 1/3 + 1/5 - 1/7 + ...
    编写一个程序，让用户指定在这种近似方法中使用迭代的次数，并且显示最终的结果。"""
    def __init__(self, times=1):
        self.times = times

    def result(self, app_value=1, value=1):
        for i in range(2, self.times+1):
            if self.times == 1:
                app_value = value
            elif i % 2 == 0:
                value += 2
                app_value = app_value - 1 / value
            else:
                value += 2
                app_value = app_value + 1 / value
        return app_value * 4


p = Pi(100)
print("迭代{0}次，π的近似值为{1}".format(p.times, p.result()))
