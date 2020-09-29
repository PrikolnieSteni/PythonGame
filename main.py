from collections import Counter


class Game(object):
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.player3 = Player()
        self.field = []
        self.field_creation(5, 6)
        self.star_game()

    def show_gamefield(self):
        print("Игровое поле:\n   0  1  2  3  4  5")
        for i in range(len(self.field)):
            print(i, self.field[i])

    def check_range(self, n, m, index):
        try:
            if self.field[n][m] == index:
                return True
        except IndexError:
            return False

    def check_dots(self, n, m, index, player):
        player = player
        nm_range = [
            (n - 1, m - 1),
            (n - 1, m + 1),
            (n, m + 1),
            (n, m - 1),
            (n + 1, m),
            (n + 1, m + 1),
            (n + 1, m - 1),
        ]
        for item in nm_range:
            if self.check_range(*item, index):
                player.score += 1

    def field_creation(self, n, m):
        self.field = [[0 for j in range(m)] for i in range(n)]
        self.show_gamefield()

    def change_field(self, n, m, player):
        if player == self.player1:
            index = 1
        elif player == self.player2:
            index = 2
        else:
            index = 3
        self.field[n][m] = index
        self.check_dots(n, m, index, player)
        self.show_gamefield()

    def field_hasvalue(self, n, m):
        if self.field[n][m] > 0:
            print("[!] Нельзя поставить фишку! Она уже занята [!]")
            return False
        else:
            return True

    def end_game(self):
        print(self.player1)
        print(self.player2)
        print(self.player3)

    def star_game(self):
        num_zeros = 1
        self.player1.turn = True
        object = self.player1
        while num_zeros != 0:
            print("Ходит:{}".format(object))
            accept = False
            while not accept:
                print("Введите координаты по x,y")

                while True:
                    try:
                        n = int(input("Введите число x: "))
                        m = int(input("Введите число y: "))
                        if -1 < n < 5 and -1 < m < 6:
                            accept = self.field_hasvalue(n, m)
                            break
                        else:
                            raise Exception()
                        continue
                    except Exception as e:
                        print('Неверный формат')
            else:
                self.change_field(n, m, object)
                num_zeros = sum(x.count(0) for x in self.field)
                object = self.change_turn()
        self.end_game()

    def change_turn(self):#поменять логику
        if self.player1.turn:
            self.player1.turn = False
            self.player2.turn = True
            object = self.player2
        elif self.player2.turn:
            self.player2.turn = False
            self.player3.turn = True
            object = self.player3
        else:
            self.player3.turn = False
            self.player1.turn = True
            object = self.player1
        return object


class Player:
    def __init__(self):
        print("\nВведите желаемое имя:")
        input_name = input()
        while type(input_name) is not str:
            print("Некоректное имя")
            break
        else:
            self.turn = False
            self.score = 0
            self.name = input_name
            print("Имя игрока:{}".format(self))

    def __str__(self):
        return f'{self.name}, текущие очки: {self.score}.'

    def change_score(self):
        self.score += 1


if __name__ == "__main__":
    Game()
