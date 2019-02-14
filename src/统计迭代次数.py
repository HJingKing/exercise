problemSizes = [1000, 2000, 4000, 10000, 100000]
print("%12s%15s" % ("Problem Size", "Iterations"))
for problemSize in problemSizes:
    pS = problemSize
    number = 0
    while problemSize > 0:
        problemSize = problemSize // 2
        number += 1
    print("%12s%15s" % (pS, number))
