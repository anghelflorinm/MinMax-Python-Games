class Player:
    def __init__(self, name):
        self.name = name
    def get_input(self):
        row = int(input("Enter row:"))
        return row
class Board:
    def __init__(self):
        self.matrix = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.matrix_row_first_available = [5, 5, 5, 5, 5, 5, 5]

    def set(self, player_key, row):
        if self.matrix_row_first_available[row] == -1:
            return False
        self.matrix[self.matrix_row_first_available[row]][row] = player_key
        self.matrix_row_first_available[row] -= 1
        return True
    def is_full(self):
        for i in self.matrix_row_first_available:
            if i != -1:
                return False
        return True
    def is_same(self, values):
        if values[0] == 0 or values[1] == 0 or values[2] == 0 or values[3] == 0:
            return False
        if values[0] == values[1] == values[2] == values[3]:
            return True
        return False

    def is_game_over(self):
        for i in range(0, 5):
            for j in range(0,4):
                if self.is_same(self.matrix[i][j : j + 4]):
                    return self.matrix[i][j]
        for j in range(0, 6):
            for i in range(0,3):
                temp = [self.matrix[i][j], self.matrix[i+1][j], self.matrix[i+2][j], self.matrix[i+3][j]]
                if self.is_same(temp):
                    return self.matrix[i][j]

        if self.is_same([self.matrix[2][0], self.matrix[3][1], self.matrix[4][2], self.matrix[5][3]]):
            return self.matrix[2][0]

        if self.is_same([self.matrix[2][6], self.matrix[3][5], self.matrix[4][4], self.matrix[5][3]]):
            return self.matrix[2][6]

        if self.is_same([self.matrix[0][3], self.matrix[1][2], self.matrix[2][1], self.matrix[3][0]]):
            return self.matrix[0][3]

        if self.is_same([self.matrix[0][3], self.matrix[1][4], self.matrix[2][5], self.matrix[3][6]]):
            return self.matrix[0][3]

        for i in range(1, 3):
            if self.is_same([self.matrix[i][i-1], self.matrix[i+1][i], self.matrix[i+2][i+1], self.matrix[i+3][i+2]]):
                return self.matrix[i][i-1]

        for i in range(0,3):
            if self.is_same([self.matrix[i][i], self.matrix[i+1][i+1], self.matrix[i+2][i+2], self.matrix[i+3][i+3]]):
                return self.matrix[i][i]

        for i in range(0, 3):
            if self.is_same([self.matrix[i][i+1], self.matrix[i+1][i+2], self.matrix[i+2][i+3], self.matrix[i+3][i+4]]):
                return self.matrix[i][i+1]
        for i in range(0, 2):
            if self.is_same([self.matrix[i][i+2], self.matrix[i+1][i+3], self.matrix[i+2][i+4], self.matrix[i+3][i+5]]):
                return self.matrix[i][i+2]
        for i in range(1, 3):
            if self.is_same([self.matrix[i][7-i], self.matrix[i+1][7-i-1], self.matrix[i+2][7-i-2], self.matrix[i+3][7-i-3]]):
                return self.matrix[i][7-i]
        for i in range(0, 3):
            if self.is_same([self.matrix[i][6-i], self.matrix[i+1][6-i-1], self.matrix[i+2][6-i-2], self.matrix[i+3][6-i-3]]):
                return self.matrix[i][6-i]
        for i in range(0, 3):
            if self.is_same([self.matrix[i][5-i], self.matrix[i+1][5-i-1], self.matrix[i+2][5-i-2], self.matrix[i+3][5-i-3]]):
                return self.matrix[i][5-i]
        for i in range(0, 2):
            if self.is_same([self.matrix[i][4-i], self.matrix[i+1][4-i-1], self.matrix[i+2][4-i-2], self.matrix[i+3][4-i-3]]):
                return self.matrix[i][5-i]

        if self.is_full() == True:
            return 3
        else:
            return 0
    def draw(self):
        print("{} {} {} {} {} {} {}\n{} {} {} {} {} {} {}\n{} {} {} {} {} {} {}\n{} {} {} {} {} {} {}\n{} {} {} {} {} {} {}\n{} {} {} {} {} {} {}\n".format(*[self.matrix[i][j] for i in range(0,6) for j in range(0,7)]))

class Game:
    def __init__(self):
        self.player1 = Player("PlayerOne")
        self.player2 = Player("PlayerTwo")
        self.board = Board()
        self.game_loop()

    def game_loop(self):
        result = 0

        pindex = 1
        while not result:
            self.board.draw()

            print("Player %d turn: " % pindex)

            coord = 0
            if pindex == 1:
                coord = self.player1.get_input()
            else:
                coord = self. player2.get_input()

            if coord < 0 or coord > 6:
                print("Incorrect coordinates")
                continue
            if not self.board.set(pindex, coord):
                print("Invalid choice")
                continue

            state = self.board.is_game_over()

            if state == 1 or state == 2:
                print("Player %d wins!" % pindex)
                break
            elif state == 3:
                print("The game ended in draw")
                break

            pindex = pindex % 2 + 1

game = Game()
