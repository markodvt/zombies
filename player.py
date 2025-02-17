from priority_queue import Priority_queue
from zombie import Zombie


class Player:
    '''Player has a name and arrow_capacity. At each round, player reloads arrows.
    '''
    def __init__(self, name, quiver_capacity, alive=True, entered_in_round = 1, killed_in_round = None, killed_by = None):
        self.name = name
        self.quiver_capacity = quiver_capacity
        self.alive = True
        self.entered_in_round = entered_in_round
        self.killed_in_round = killed_in_round
        self.killed_by = killed_by
        self.remaining_arrows = 0
        
    def __repr__(self):
        # return self.__class__.__name__ + str(self.__dict__)
        print_keys = ('name', 'alive', 'quiver_capacity', 'killed_in_round', 'killed_by')
        result = self.__class__.__name__ + '{' 
        result += ', '.join(f'{k}: {self.__dict__[k]}' for k in print_keys)
        result += '}'
        return result

    def killed(self, zombie, round=None):
        if not(self.alive):
            raise RuntimeError(f'Player {self.name} previously killed by {self.killed_by}; cannot be killed again by {zombie}.')
        else:
            self.alive = False
            self.killed_by = zombie
            self.killed_in_round = round

    @classmethod
    def TestMe(cls):
        print(f'\n{'='*40}\nTesting class: {cls.__name__}\n{'='*40}')

        player1 = Player('Steve', 20)
        player2 = Player('Jimmy', 50)
        zombie = Zombie('Zack', 0, 20, 10)

        print(f'Players ........\n{player1}\n{player2}')
        print(f'\nUpdate:  Player 1 gets killed by a zombie named Zack in Round 6\n')
        player1.killed(zombie, 6)
        print(f'Players ........\n{player1}\n{player2}')
        
        
def main():
    Player.TestMe()

if __name__ == '__main__':
    main()

