import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建飞船
    ship = Ship(ai_setting, screen)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.checkz_events(ship)
        ship.update()
        # 每次循环时都重新绘制屏幕
        # 让最近绘制的屏幕可见
        gf.update_screen(ai_setting, screen, ship)

run_game()