# 递归
"""
1.函数内部自己调用自己
2.必须要有出口
"""
# 从给定数开始递减一直求和到1的函数
def sumNum(num):
    # 出口
    if num == 1:
        return 1
    return num + sumNum(num-1)

print(sumNum(6))