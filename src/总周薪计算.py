class Emolument(object):
    """一个雇员一周的总薪水，等于其每小时的薪水乘以一周正常工作的小时数，再加上加班费。
    加班费等于总的加班时间乘以每小时薪水的1.5倍。编写一个程序， 以每小时的薪水、总的常规工作时间和总的加班时间作为参数，
    并且显示一个雇员的总周薪"""
    def __init__(self, salary):
        self.salary = salary

    def weekly_wage(self, working_time, overtime):
        ww = self.salary * working_time + self.salary * 1.5 * overtime
        return ww


e = Emolument(200.522)
print("该雇员的总周薪为：{0:.2f}".format(e.weekly_wage(35, 15)))
