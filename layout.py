from random import choice
from color import *
from modules import Building
from drawer import Block


class Layout:
    """棋盘"""

    def __init__(self, x_count=16, y_count=22, raw_speed=3):
        """layout用1表示有物体存在, old_buildings用数字表示颜色, 0表示不是积木"""
        self.block_x_count = x_count
        self.block_y_count = y_count
        self.raw_speed = raw_speed
        self.score = 0      # 分数, 每消除一行加一
        self.layout = [
                [0 if 1 < i < self.block_x_count - 2 and j < self.block_y_count - 2
                    else 1 
                    for i in range(self.block_x_count)
                    ] for j in range(self.block_y_count)
            ]
        self.old_buildings = [[0 for i in range(self.block_x_count)] for j in range(self.block_y_count)]

    @property
    def size(self):
        """返回棋盘屏幕大小(width,height)"""
        return (self.block_x_count * Block.width,
                self.block_y_count * Block.height)

    def get_score(self):
        return self.score

    def create_new_building(self):
        """
        创建新的积木,初始化位置为第5,0格, 速度为4
        :return: 返回是否无空间创建了
        """
        self.building = Building()
        self.building_left, self.building_top = self.block_x_count//2 - 3, 0  #
        self.drop_speed = self.raw_speed
        # print(self.test_building_touch_wall(), self.building_left)
        return self.test_building_touch_wall()

    @property
    def speed(self):
        return self.drop_speed

    def test_building_touch_wall(self, x_offset=0, y_offset=0):
        """
        积木是否已经触底/墙壁
        具体操作：
        判断积木最后一排的1,是否在当前棋牌对应的位置是也是1
        @:param x_offset: x的偏移量 移动时可以传入1/-1来判断
        @:param y_offset: y的偏移量 正常下落时可以传入1来判断
        """
        for i in range(4, -1, -1):
            for j in range(5):
                if self.building[i][j]:
                    if self.layout[
                        i + self.building_top +y_offset][
                            j + self.building_left +x_offset]:
                        return True
        return False

    def move_left_right(self, x):
        """
        左右移动
        @:param x: 移动量 x_offset
        """
        #: 移动时不能撞墙
        if not self.test_building_touch_wall(x_offset=x):
            self.building_left += x

    def down_build(self):
        """ 盒子的自动下移 """
        self.building_top += 1

    def direct_down(self):
        """ 手动快速降落 """
        self.drop_speed = 50

    def convert_building(self):
        """
        * 扭转盒子的总方位 (右转)
        具体操作：
        把第一竖排的倒序给第一横排的
        把第二竖排的倒序给第二横排的
        后面同理.
        """
        new_box = [[0 for i in range(5)] for j in range(5)]
        for i in range(5):
            for j in range(4, -1, -1):
                new_box[i][j] = self.building[4 - j][i]
        self.building.change_to(new_box)

    def clear_full_lines(self):
        """消除满行的所有行"""
        new_layout = [
            [
                0 if 1 < i < self.block_x_count - 2 and j < self.block_y_count - 2
                else 1 for i in range(self.block_x_count)
            ] for j in range(self.block_y_count)
        ]
        new_buildings = [[0 for i in range(self.block_x_count)] for j in range(self.block_y_count)]

        row_len = self.block_x_count - 4
        new_row = self.block_y_count - 2 - 1
        for cur_row in range(self.block_y_count - 2 - 1, 0, -1):
            if sum(self.layout[cur_row][2:self.block_x_count - 2]) < row_len:
                new_layout[new_row] = self.layout[cur_row]
                new_buildings[new_row] = self.old_buildings[cur_row]
                new_row -= 1
            else:
                self.score += 1
        self.layout = new_layout
        self.old_buildings = new_buildings
        

    def put_building_to_layout(self):
        """将积木放到棋盘里"""
        for i in range(4, -1, -1):
            for j in range(5):
                if self.building[i][j]:
                    x, y = i + self.building_top, j + self.building_left
                    self.layout[x][y] = 1
                    self.old_buildings[x][y] = COLORS.index(self.building.get_color()) + 1
        #: 这里会调用消除函数
        self.clear_full_lines()

    def draw_building(self, s):
        """
        显示积木
        @:param s : pygame = screen 
        """
        cur_left, cur_top = self.building_left * Block.width, self.building_top * Block.height
        for i in range(5):
            for j in range(5):
                # 只画积木实体,不管盒子本身
                if self.building[j][i]:
                    Block.draw(s, cur_left + i * Block.width,
                               cur_top + j * Block.height, 
                               self.building.get_color(),
                               COLOR_WHITE
                    )

    def draw(self, s):
        """
        显示棋盘
        @:param s : pygame = screen 
        """
        for i in range(self.block_x_count):
            for j in range(self.block_y_count):
                # 空白位置
                if self.layout[j][i] == 0:
                    Block.draw(s, i * Block.width, j * Block.height,
                               COLOR_WHITE, COLOR_BLACK)
                else: 
                    # 墙体
                    if self.old_buildings[j][i] == 0 :
                        Block.draw(s, i * Block.width, j * Block.height,
                                COLOR_BLACK, COLOR_WHITE)
                    # 旧的积木
                    else:
                        color = COLORS[self.old_buildings[j][i] - 1]
                        Block.draw(s, i * Block.width, j * Block.height,
                                color, COLOR_BLACK)
