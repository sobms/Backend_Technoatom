import random
import numpy as np
from Exceptions import InputError

class TicTacGame:

    d = {1:'X',2:'O',0:' '}

    def __init__(self, player1 ='player1', player2 = 'player2', size = 3):
        self.player1 = player1
        self.player2 = player2
        self.size = size
        self.markers = {1:self.player1, 2:self.player2}
        self.field = np.zeros([self.size,self.size])

    def show_board(self):
        print('+---' * self.field.shape[1] + '+')
        for i in range(0,self.field.shape[1]):
            print(('| {} ' * self.field.shape[1] + '|').format(*[self.d[i] for i in self.field[i,:]]))
            print('+---' * self.field.shape[1] + '+')

    def players_move(self, player):
        print('Make your move {}'.format(player))
        while (True):
            values = input().split(',')
            marker = (2 if player==self.player2 else 1)
            try:
                self.validate_input(values, marker)
                break
            except InputError as input_err:
                print(input_err)

    def validate_size(self, size): #test
        if not size.isdigit():
            raise InputError('Wrong input!')
        elif int(size)>20 or int(size)<3:
            raise InputError('Wrong input! Size more or less than acceptable value!')
        else:
            self.size = int(size)
            self.field = np.zeros([self.size,self.size])

    def validate_input(self, values, marker): #test
        if len(values) != 2:
            raise InputError('Wrong input! Incorrect number of elements!')
        for i in values:
            if not i.isdigit() or int(i)>self.field.shape[1] or int(i)<1:
                raise InputError('Wrong input! Incorrect values.')

        _x, _y = values
        if self.field[int(_y)-1][int(_x)-1]!=0:
            raise InputError('Wrong input! Cell is already filled!')
        self.field[int(_y)-1][int(_x)-1] = marker

    def start_game_p_vs_p(self):
        print('Please, type player1 name')
        self.player1 = input()
        print('Please, type player2 name')
        self.player2 = input()
        self.markers = {1:self.player1, 2:self.player2}
        print('Please, enter size of field')
        while(True):
            size = input()
            try:
                self.validate_size(size)
                break
            except InputError as input_err:
                print(input_err)

        player = self.player1 if random.randint(1,2)==1 else self.player2
        winner = False
        while (not winner):
            self.players_move(player)
            self.show_board()
            player = self.player1 if player==self.player2 else self.player2
            winner = self.check_winner()
        if winner != 'End of game':
            print(winner + ' is WINNER!')
        else:
            print(winner)

    def check_winner(self): #test
        winner = False
        dim = np.shape(self.field)[1]
        if np.all(self.field!=0):
            winner = 'End of game'
        if np.all((self.field.diagonal()) == self.field[0,0]) and (self.field[0,0] != 0):
            winner = self.markers[self.field[0,0]]
        if (np.sum([self.field[dim-i][i-1]==self.field[dim-1,0] for i in range(1,dim+1)])==dim) and self.field[dim-1,0]!=0:
            winner = self.markers[self.field[dim-1,0]]
        for i in range(0,dim):
            if np.all(self.field[i,:] == self.field[i,0]) and self.field[i,0]!=0: #i-ая строка
                winner = self.markers[self.field[i,0]]
            if np.all(self.field[:,i] == self.field[0,i]) and self.field[0,i]!=0: #i-ый столбец
                winner = self.markers[self.field[0,i]]
        return winner

if __name__ == '__main__':
    game = TicTacGame()
    game.start_game_p_vs_p()
