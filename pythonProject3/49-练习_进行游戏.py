# 定义一个游戏类
class Game(object):
    # 类属性 历史最高分
    top_score = 0

    # 初始化游戏信息
    def __init__(self, player_name):
        self.player_name = player_name

    # 游戏帮助信息
    @staticmethod
    def show_help():
        print('游戏帮助信息...')

    # 展示历史最高分
    @classmethod
    def show_top_score(cls):
        print(f'历史最高分：{cls.top_score}')

    # 开始游戏
    def start_game(self):
        print(f'{self.player_name}玩家开始游戏。')

    # 结束游戏
    def end_game(self, score):
        if score > Game.top_score:
            Game.top_score = score
        print(f'游戏结束，{self.player_name}获得了{score}分。')

Game.show_top_score()

game1 = Game('player1')
game1.start_game()
game1.end_game(30)
Game.show_top_score()
