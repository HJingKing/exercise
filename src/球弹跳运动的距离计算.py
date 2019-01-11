class Ball(object):
    """一个标准的科学实验是，抛球并且看它能够弹跳多高。一旦球的“弹跳性”已经确定了，这个比率值就会给出弹跳性的指数。
    例如：如果球从10米高下弹跳到6米高，这个索引就是0.6，并且球在一次弹跳之后总的运动距离是16米。如果球继续弹跳，
    两次弹跳后的距离将会是10米+6米+6米+3.6米=25.6米。注意，每次后续的弹跳运动的距离，都是到地板的距离加上这个距离的0.6倍，
    这个0.6倍就是球反弹回来的距离。编写一个程序，让用户输入球的一个初始高度以及运行球持续弹跳的次数。输出应该是球所运动的总距离。"""
    def __init__(self):
        self.ini_height = 0
        self.bouncing_times = 0

    def set_ini_height(self):
        while True:
            try:
                ini_height = input("请输入球的初始高度：")
                self.ini_height = float(ini_height)
                break
            except ValueError:
                print("请输入数字！！！")

    def set_bouncing_times(self):
        while True:
            try:
                bouncing_times = input("请输入球的持续弹跳次数：")
                self.bouncing_times = int(bouncing_times)
                break
            except ValueError:
                print("请输入整数！！！")

    def total_distance(self, distance=0):
        if self.bouncing_times > 0:
            a_distance = self.ini_height * 0.6
            distance = distance + self.ini_height + a_distance
            self.bouncing_times -= 1
            self.ini_height = a_distance
            return self.total_distance(distance)
        else:
            return distance


b = Ball()
b.set_ini_height()
b.set_bouncing_times()
print("该球所运动的总距离为：{}米".format(b.total_distance()))
