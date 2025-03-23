# 猜数游戏
import random
pc_num = random.randint(0, 999)
pl_num = int(input('这是一个猜数游戏，你共有10次机会。\n请在0-999之间猜一个数：'))
i = 1
while i < 10:
    if pl_num > pc_num:
        print(f'{pl_num}大了。')
    elif pl_num < pc_num:
        print(f'{pl_num}小了。')
    else:
        print(f'恭喜你猜对了，数字是{pl_num}！')
        break

    pl_num = int(input(f'你还剩{10 - i}次机会，请输入你要猜的数字：'))
    i += 1

if i >= 10:
    print(f'很遗憾，次数已用完。正确数字是：{pc_num}。')