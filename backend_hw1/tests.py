import unittest
import numpy as np
from Exceptions import InputError
from backend_homework1 import TicTacGame

class TicTacTest(unittest.TestCase):
    def setUp(self):
        self.game = TicTacGame()
        
    def test_validate_size(self):
        with self.assertRaises(InputError):
            self.game.validate_size('21')

        with self.assertRaises(InputError):
            self.game.validate_size('2.1')

        with self.assertRaises(InputError):
            self.game.validate_size('2')

        self.game.validate_size('15')
        self.assertEqual(self.game.size,15)

    def test_validate_input(self):
        with self.assertRaises(InputError):
            self.game.validate_input(['1',' 2'],1)

        with self.assertRaises(InputError):
            self.game.validate_input(['1.2'],1)

        self.game.validate_input(['3','3'],1)
        arr = np.array([[0,0,0],[0,0,0],[0,0,1]])
        for i in range(0,self.game.field.shape[1]):
            for j in range(0,self.game.field.shape[1]):
                self.assertEqual(self.game.field[i][j], arr[i][j])

        with self.assertRaises(InputError):
            self.game.validate_input(['3','3'],1)

        self.game = TicTacGame('M','N',6)
        with self.assertRaises(InputError):  
            self.game.validate_input(['7','6'],1)
    
    def test_check_winner(self):
        self.game.field = np.array([[1,1,1],[2,1,2],[1,2,2]])
        self.assertEqual(self.game.check_winner(), 'player1')
        self.game.field = np.array([[2,1,1],[2,1,2],[2,2,1]])
        self.assertEqual(self.game.check_winner(), 'player2')
        self.game.field = np.array([[2,1,1],[2,1,2],[1,2,1]])
        self.assertEqual(self.game.check_winner(), 'player1')
        self.game.field = np.array([[2,1,1],[1,1,2],[2,2,1]])
        self.assertEqual(self.game.check_winner(), 'End of game')

if __name__ == '__main__':
    unittest.main()