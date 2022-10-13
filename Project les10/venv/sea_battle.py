''' Морской бой через классы'''
import random
class SeaMap:
    def __init__(self):
        self.field = [['.' for y in range(10)] for x in range(10)]
    def shoot(self, row, col, result):
        self.field[row][col] = '*'
        for i in range(10):
            print(self.field[i])
        if result == 'miss':
            print('Промах!')
        elif result == 'hit':
            print('Попал!')
        elif result == 'sink':
            print('Потопил :(')
    def cell(self, row, col):
        # self.row = row
        # self.col = col
        shoot = random.choice([1, 2, 3])
        if shoot == 1:
            self.field[row][col] = '.'
        elif shoot == 2:
            self.field[row][col] = '*'
        elif shoot == 3:
            self.field[row][col] = 'X'
        return [print(self.field[i]) for i in range(10)]



sm = SeaMap()
sm.shoot(2, 0, 'miss')
sm.shoot(6, 9, 'miss')
sm.cell(5, 5)


