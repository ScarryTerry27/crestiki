class Cell:
    def __init__(self, name=False):
        self.name = name


class Field:
    def __init__(self):
        self.field = [[Cell() for _ in range(3)] for i in range(3)]


class Game:
    def __init__(self):
        self.game = Field()
        self.sb = True
        self.symbols = ['O', 'X']
        self.show()
        print('Первым ходит X')

    def step(self, x, y):
        if not isinstance(x, int) or not isinstance(y, int) or not all((0 <= x < 3, 0 <= y < 3)):
            print('неверный формат числа')
        else:
            return self.go_step(x, y)

    def go_step(self, x, y):
        if self.game.field[x][y].name:
            print('Ячейка уже занята')
        else:
            self.game.field[x][y].name = self.symbols[self.sb]
            res = self.check_win(self.symbols[self.sb])
            self.sb = not self.sb
            if res:
                print(res)
                print('Игра окончена! Создайте новую игру')
                return 'Game over'
            else:
                if self.check_draw():
                    print('Игра окончена! Победила дружба!')
                    return 'Draw'

        self.show()
        print(f'Следующий ход {self.symbols[self.sb]}')

    def check_win(self, sym):
        field = self.game.field
        for line in field:
            if set([item.name for item in line]) == {f'{sym}'}:
                return f'Победили {sym}'

        lst = [[(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]
        for line in lst:
            if set([field[i[0]][i[1]].name for i in line]) == {f'{sym}'}:
                return f'Победили {sym}'

        lst = [[(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(2, 0), (2, 1), (2, 2)]]
        for line in lst:
            if set([field[i[0]][i[1]].name for i in line]) == {f'{sym}'}:
                return f'Победили {sym}'

        return False

    def check_draw(self):
        for line in self.game.field:
            for item in line:
                if not item.name:
                    return False
        return True

    def show(self):
        for line in self.game.field:
            for item in line:
                if item.name:
                    print(item.name.rjust(2, ' '), end=' ')
                else:
                    print('__', end=' ')
            print()


game = Game()
while True:
    res = game.step(*map(int, input().split()))
    if res in ('Game over', 'Draw'):
        break






