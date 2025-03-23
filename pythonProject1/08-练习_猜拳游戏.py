# 案例：与电脑玩石头剪刀布
import random  # import导入模块（module）,用模块后加“.”的方式使用模块内函数
# 如下文的random.randint函数
print('游戏：石头剪刀布')
play_num = int(input('请输入你要出的手势对应的数字：（0-石头、1-剪刀、2-布）\n'))
pc_num = random.randint(0, 2)  # 0-2之间的整数
if play_num == 0:
    play_ges = '石头'
elif play_num == 1:
    play_ges = '剪刀'
else:
    play_ges = '布'

if pc_num == 0:
    pc_ges = '石头'
elif pc_num == 1:
    pc_ges = '剪刀'
else:
    pc_ges = '布'

print(f'你的手势为：{play_ges}')
print(f'电脑的手势为：{pc_ges}')
if play_num - pc_num == 0:
    print('平局！')
elif play_num - pc_num == -1 or play_num - pc_num == 2:
    print('玩家获胜！')
else:
    print('电脑获胜！')