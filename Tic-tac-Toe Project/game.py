import time
from player import HumanPlayer, RandomComputerPlayer
class TicTacToe:
    def __init__(self):
        self.board = [' ' for i in range(9)]  # we are using a single list to represnt a 3*3 board
        self.current_winner = None # keep track of the winner

    def print_board(self):
        #this is just getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 (tells us  what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    def available_moves(self):
        #return
        moves = []
        for (i,spot) in enumerate(self.board):
            if spot == " ":
                moves.append(i)
        return moves
    def empty_squares(self):
        return ' ' in self.board
    def num_empty_squares(self):
        return self.count.board(" ")
    def make_move(self,square,letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        return False
    def winner(self,square,letter):
        row_ind = square // 3
        row = self.board[row_ind*3: (row_ind + 1)*3]
        if all([spot == letter for spot in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        if square % 2== 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

def play(game,x_player,o_player,print_game=True):
    if print_game:
        game.print_board_nums()
    letter = 'x' #starting letter
    while game.empty_squares():
        if letter == 'x':
            square = x_player.get_move(game)
        else:
            square = o_player.get_move(game)
        if game.make_move(square,letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')
            if game.current_winner:
                if print_game:
                    print(letter + 'Wins!')
                return letter
            letter = 'o' if letter == 'x' else 'x'
        time.sleep(0.8)
    if print_game:
        print('It\'s a tie')
if __name__ == '__main__':
    x_player = HumanPlayer('x')
    o_player = RandomComputerPlayer('o')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)