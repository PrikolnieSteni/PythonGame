from collections import Counter

class GameField(object):
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.player3 = Player()
        self.field = {}
        self.field_creation(5, 6)
        self.star_game()

    def show_gamefield(self):
        print("Игровое поле:\n   0  1  2  3  4  5")
        for i in range(len(self.field)):
            print(i, self.field[i])

    def field_creation(self, n, m):
        self.field = [[0 for j in range(m)] for i in range(n)]
        self.show_gamefield()

    def count_score(self, n, m, index, obj):
        object = obj
        try:
            if self.field[n][m-1] == index:
                object.score += 1
            if self.field[n][m+1] == index:
                object.score += 1
        except IndexError:
                print("[!] Неправильные координаты")



    def change_field(self, n, m, obj):
                if obj == self.player1:
                    index = 1
                elif obj == self.player2:
                    index = 2
                else:
                    index = 3
                self.field[n][m] = index
                self.count_score(n,m,index,obj)
                self.show_gamefield()

    def field_hasvalue(self, n, m):
        if self.field[n][m] == 1 or self.field[n][m] == 2 or self.field[n][m] == 3:
            print("[!] Нельзя поставить фишку! Она уже занята [!]")
            return False
        else:
            return True

    def star_game(self):
        num_zeros = 1
        self.player1.turn = True
        object = self.player1
        while num_zeros != 0:
            print("Ходит игрок: {}, Текущие очки: {}".format(object.name , object.score))
            accept = False
            while accept == False:
                print("Введите координаты по x,y")
                while True:
                    try:
                        n = int(input("Введите число x: "))
                        m = int(input("Введите число y: "))
                        if -1 < n < 5 and -1 < m < 6:
                            raise Exception()
                        break
                    except Exception as e:
                        print('Неверный формат')
                accept = self.field_hasvalue(n, m)
            else:
                self.change_field(n, m, object)
                num_zeros = Counter('0')
                object = self.change_turn()

    def change_turn(self):
        if self.player1.turn == True:
            self.player1.turn = False
            self.player2.turn = True
            object = self.player2
        elif self.player2.turn == True:
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
        while type(input_name) is not  str:
            print("Некоректное имя")
            break
        else:
            self.turn = False
            self.score = 0
            self.name = input_name
            self.show_playerinfo()

    def show_playerinfo(self):
        print("Имя игрока: {}, Текущие очки: {}".format(self.name, self.score))

    def change_score(self):
        self.score +=1

if __name__ == "__main__":
    GameField()