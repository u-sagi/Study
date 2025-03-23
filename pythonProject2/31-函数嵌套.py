# 函数嵌套：在一个函数里又调用了另一个函数
def funcB():
    print('funcB函数代码...')


def funcA():
    print('-' * 40)
    print('funcA函数代码...')
    funcB()  # funcA函数嵌套funcB函数
    print('-' * 40)

# 调用funcA函数
funcA()

