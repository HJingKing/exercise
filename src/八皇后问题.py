"""八皇后问题，是一个古老而著名的问题，是回溯算法的典型案例。
    该问题是国际西洋棋棋手马克斯·贝瑟尔于1848年提出：
    在8×8格的国际象棋上摆放八个皇后，使其不能互相攻击，
    即任意两个皇后都不能处于同一行、同一列或同一斜线上，问有多少种摆法。"""
import random


def conflict(state, nextx):  # state为已摆放的棋子的位置的元组，比如（1,3,0）
    """定义冲突函数,state为元组，nextx为下一个皇后的水平位置，nexty为下一个皇后的垂直位置"""
    nexty = len(state)  # 获取当前行号
    for i in range(nexty):  # 检查每一个已摆放的棋子和当前行要摆放的棋子的位置（nextX, nextY）是否冲突
        if abs(state[i]-nextx) in (0, nexty-i):
            # 关键！若是两个棋子 行差值 的绝对值 出现在元组 （0，行差值）中，则冲突发生，返回True
            # 若下一个皇后和前面的皇后列相同或者在一条对角线上，则冲突
            return True
    return False  # 无冲突，可行的摆放位置


def queens(num=8, state=()):  # num为棋盘的行数，state为已摆放的棋子的列数汇总，类型为元组
    """八皇后问题，这里num表示规模"""
    for pos in range(num):  # pos从 0 到 棋盘行数 - 1
        if not conflict(state, pos):
            # 位置不冲突
            # 检查是否冲突
            if len(state) == num - 1:
                # 检查是否最后一行，如果是最后一行，则执行终极操作，不再递归
                # 若是最后一个皇后，则返回该位置
                yield (pos,)  # 没有冲突，返回列数的元组
            else:  # 若不是最后一个皇后，则将该位置返回到state元组并传给后面的皇后
                for result in queens(num, state + (pos,)):
                    # 递归调用queens，不过找到了更多的一行的摆放位置，所以，加上（pos,）
                    # 如果是最后一行，返回一个数字的元组，比如，（2）
                    # 此时，如果pos为0，那么，倒数第二行返回的为两个数字的元组，比如，（0, 2）
                    # 调用每返回一层，返回的元组的长度就加1，直到最后用户在外部调用queens的位置
                    # 返回所有行的皇后位置的 元组，其长度为行数
                    yield (pos,) + result


def prettyprint(solution):
    """打印函数"""
    def line(pos, length=len(solution)):
        """打印一行，皇后位置用X填充，其余用0填充"""
        return 'O'*pos+'X'+'O'*(length-pos-1)
    for pos in solution:
        print(line(pos))


# 随机打印一种
prettyprint(random.choice(list(queens(8))))
